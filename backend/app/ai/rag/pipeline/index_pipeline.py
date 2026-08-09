import hashlib
from typing import Iterable, List

from .base import BasePipeline
from .chunker import FixedLengthChunker
from .embedding_pipeline import EmbeddingPipeline
from .schema import DocumentChunk


class IndexPipeline(BasePipeline):
    """
    Document indexing pipeline.

    Flow:

        Document
            |
            v
        Chunking
            |
            v
        Embedding
            |
            v
        Vector Store
    """

    def __init__(
        self,
        embedding=None,
        vector_store=None,
        chunker=None,
        collection_name="grayproject",
        embedding_batch_size=32,
        embedding_cache=None,
    ):
        self.embedding = embedding
        self.vector_store = vector_store
        self.collection_name = collection_name
        self.embedding_batch_size = embedding_batch_size
        self.embedding_cache = embedding_cache

        self.chunker = chunker if chunker else FixedLengthChunker()

        if self.vector_store:
            self._ensure_collection()

    def _ensure_collection(self):
        if hasattr(
            self.vector_store,
            "create_collection",
        ):
            self.vector_store.create_collection(self.collection_name)

        if hasattr(
            self.vector_store,
            "use_collection",
        ):
            self.vector_store.use_collection(self.collection_name)

    def create_chunks(
        self,
        documents,
    ) -> List[DocumentChunk]:
        chunks = []

        for doc in documents:
            chunks.extend(self._create_document_chunks(doc))

        return chunks

    def _create_document_chunks(
        self,
        document,
    ) -> List[DocumentChunk]:
        document_id = hashlib.sha1(document.page_content.encode("utf-8")).hexdigest()

        chunks = []

        texts = self.chunker.split(document.page_content)

        for index, chunk in enumerate(texts):
            chunks.append(
                DocumentChunk(
                    id=f"{document_id}_{index}",
                    document_id=document_id,
                    text=chunk.content,
                    metadata={
                        **document.metadata,
                        **chunk.metadata,
                    },
                )
            )

        return chunks

    def iter_chunks(
        self,
        documents: Iterable,
    ):
        """
        Stream document chunks without accumulating
        all chunks in memory.
        """
        for document in documents:
            yield from self._create_document_chunks(document)

    def run(self, documents):
        chunks = self.create_chunks(documents)

        return self._index_chunks(
            chunks,
            document_count=len(documents),
        )

    def run_stream(
        self,
        documents: Iterable,
    ):
        """
        Stream documents through the indexing pipeline.

        Documents are processed incrementally so the
        complete document set and complete chunk set
        do not need to stay in memory.
        """
        document_count = 0
        chunk_count = 0
        batch = []

        for chunk in self.iter_chunks(documents):
            document_count += 1 if chunk.metadata.get("chunk_id") == 0 else 0

            batch.append(chunk)

            if len(batch) >= self.embedding_batch_size:
                self._index_chunk_batch(batch)
                chunk_count += len(batch)
                batch = []

        if batch:
            self._index_chunk_batch(batch)
            chunk_count += len(batch)

        return {
            "documents": document_count,
            "chunks": chunk_count,
        }

    def _index_chunks(
        self,
        chunks: List[DocumentChunk],
        document_count: int,
    ):
        for start in range(
            0,
            len(chunks),
            self.embedding_batch_size,
        ):
            batch = chunks[start : start + self.embedding_batch_size]

            self._index_chunk_batch(batch)

        return {
            "documents": document_count,
            "chunks": len(chunks),
        }

    def _index_chunk_batch(
        self,
        chunks: List[DocumentChunk],
    ):
        if not chunks:
            return

        if self.embedding is None:
            return

        embedding_pipeline = EmbeddingPipeline(
            embedding=self.embedding,
            cache=self.embedding_cache,
        )

        embedded_chunks = embedding_pipeline.run(
            chunks,
            batch_size=len(chunks),
        )

        if self.vector_store:
            self.vector_store.add(embedded_chunks)

    def add_document(self, document):
        """
        Add single document.
        """

        return self.run([document])

    def update_document(self, document):
        """
        Update existing document.

        Remove all existing chunks belonging to the
        same source, then rebuild the document index.
        """

        if self.vector_store:
            source = document.metadata.get("source")

            if source and hasattr(
                self.vector_store,
                "delete_by_source",
            ):
                self.vector_store.delete_by_source(source)

        return self.run([document])

    def delete_document(self, document_id: str):
        if self.vector_store:
            if hasattr(
                self.vector_store,
                "delete_by_document_id",
            ):
                self.vector_store.delete_by_document_id(document_id)
            else:
                self.vector_store.delete(document_id)

        return {"deleted": document_id}

    def delete_by_source(self, source: str):
        if self.vector_store is not None:
            if hasattr(
                self.vector_store,
                "delete_by_source",
            ):
                self.vector_store.delete_by_source(source)

        return {"deleted_source": source}
