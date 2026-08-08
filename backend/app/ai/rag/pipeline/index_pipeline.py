import hashlib
from typing import List

from .base import BasePipeline
from .chunker import FixedLengthChunker
from .schema import (
    DocumentChunk,
    EmbeddedChunk,
)


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
    ):
        self.embedding = embedding

        self.vector_store = vector_store

        self.collection_name = collection_name

        self.chunker = chunker if chunker else FixedLengthChunker()
        if self.vector_store:
            self._ensure_collection()

    def _ensure_collection(self):
        if hasattr(self.vector_store, "create_collection"):
            self.vector_store.create_collection(self.collection_name)

        if hasattr(self.vector_store, "use_collection"):
            self.vector_store.use_collection(self.collection_name)

    def create_chunks(
        self,
        documents,
    ) -> List[DocumentChunk]:
        chunks = []

        for doc in documents:
            document_id = hashlib.sha1(doc.page_content.encode("utf-8")).hexdigest()

            texts = self.chunker.split(doc.page_content)

            for index, chunk in enumerate(texts):
                chunks.append(
                    DocumentChunk(
                        id=f"{document_id}_{index}",
                        document_id=document_id,
                        text=chunk.content,
                        metadata={
                            **doc.metadata,
                            **chunk.metadata,
                        },
                    )
                )

        return chunks

    def run(self, documents):
        chunks = self.create_chunks(documents)

        if self.embedding:
            vectors = self.embedding.embed_documents([chunk.text for chunk in chunks])

        else:
            vectors = None

        if self.vector_store:
            records = []

            for chunk, vector in zip(chunks, vectors or []):
                records.append(
                    EmbeddedChunk(
                        id=chunk.id,
                        document_id=chunk.document_id,
                        text=chunk.text,
                        embedding=vector,
                        metadata=chunk.metadata,
                    )
                )

            self.vector_store.add(records)

        return {
            "documents": len(documents),
            "chunks": len(chunks),
        }

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
            if hasattr(self.vector_store, "delete_by_document_id"):
                self.vector_store.delete_by_document_id(document_id)
            else:
                self.vector_store.delete(document_id)

        return {"deleted": document_id}

    def delete_by_source(self, source: str):
        if self.vector_store is not None:
            if hasattr(self.vector_store, "delete_by_source"):
                self.vector_store.delete_by_source(source)

        return {"deleted_source": source}
