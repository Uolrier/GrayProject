import hashlib
from concurrent.futures import ThreadPoolExecutor
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
        parallel_workers=4,
    ):
        self.embedding = embedding
        self.vector_store = vector_store
        self.collection_name = collection_name
        self.embedding_batch_size = embedding_batch_size
        self.embedding_cache = embedding_cache
        self.parallel_workers = max(1, parallel_workers)

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
                        "chunk_id": index,
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

    def run_parallel(
        self,
        documents: Iterable,
        max_workers: int | None = None,
    ):
        """
        Build the index using parallel embedding workers.

        Chunk creation remains lightweight and deterministic.
        Embedding batches are processed concurrently, while
        vector-store writes remain serialized.
        """
        if self.embedding is None:
            return {
                "documents": 0,
                "chunks": 0,
            }

        workers = self.parallel_workers if max_workers is None else max_workers

        if workers <= 0:
            raise ValueError("max_workers must be greater than zero")

        batches = []
        document_count = 0
        batch = []

        for document in documents:
            document_count += 1

            for chunk in self._create_document_chunks(document):
                batch.append(chunk)

                if len(batch) >= self.embedding_batch_size:
                    batches.append(batch)
                    batch = []

        if batch:
            batches.append(batch)

        if not batches:
            return {
                "documents": document_count,
                "chunks": 0,
            }

        chunk_count = 0

        with ThreadPoolExecutor(
            max_workers=workers,
        ) as executor:
            futures = [
                executor.submit(
                    self._embed_chunk_batch,
                    current_batch,
                )
                for current_batch in batches
            ]

            # Consume results in submission order.
            # This keeps indexing deterministic even though
            # embedding work executes concurrently.
            for future in futures:
                embedded_chunks = future.result()

                self._store_embedded_chunks(embedded_chunks)

                chunk_count += len(embedded_chunks)

        return {
            "documents": document_count,
            "chunks": chunk_count,
        }

    def _embed_chunk_batch(
        self,
        chunks: List[DocumentChunk],
    ):
        """
        Embed one chunk batch.

        This method is executed by parallel workers.
        """
        if not chunks:
            return []

        if self.embedding is None:
            return []

        embedding_pipeline = EmbeddingPipeline(
            embedding=self.embedding,
            cache=self.embedding_cache,
        )

        return embedding_pipeline.run(
            chunks,
            batch_size=len(chunks),
        )

    def _store_embedded_chunks(
        self,
        chunks,
    ):
        """
        Store embedded chunks serially.

        Vector stores are deliberately kept outside the
        worker threads to avoid concurrent writes.
        """
        if not chunks:
            return

        if self.vector_store:
            self.vector_store.add(chunks)

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

        embedded_chunks = self._embed_chunk_batch(chunks)

        self._store_embedded_chunks(embedded_chunks)

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
