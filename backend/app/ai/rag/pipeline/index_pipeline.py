from typing import List

from .base import BasePipeline
from .chunker import FixedLengthChunker
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
    ):
        self.embedding = embedding
        self.vector_store = vector_store

        self.chunker = chunker if chunker else FixedLengthChunker()

    def create_chunks(
        self,
        documents,
    ) -> List[DocumentChunk]:
        chunks = []

        for doc in documents:
            texts = self.chunker.split(doc.content)

            for index, text in enumerate(texts):
                chunks.append(
                    DocumentChunk(
                        id=f"{doc.id}_{index}",
                        document_id=doc.id,
                        text=text,
                        metadata=doc.metadata,
                    )
                )

        return chunks

    def run(self, documents):
        chunks = self.create_chunks(documents)

        if self.embedding:
            vectors = self.embedding.embed([chunk.text for chunk in chunks])

        else:
            vectors = None

        if self.vector_store:
            self.vector_store.add(
                chunks,
                vectors,
            )

        return {
            "documents": len(documents),
            "chunks": len(chunks),
        }
