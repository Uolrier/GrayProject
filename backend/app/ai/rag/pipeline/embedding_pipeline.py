from typing import List

from .batch import batch_split
from .schema import DocumentChunk, EmbeddedChunk


class EmbeddingPipeline:
    """
    Convert document chunks into embedded chunks.
    """

    def __init__(self, embedding):
        self.embedding = embedding

    def run(
        self,
        chunks: List[DocumentChunk],
        batch_size: int = 32,
    ) -> List[EmbeddedChunk]:
        embedded_chunks = []

        for batch in batch_split(
            chunks,
            batch_size,
        ):
            texts = [chunk.text for chunk in batch]

            vectors = self.embedding.embed_documents(texts)

            for chunk, vector in zip(
                batch,
                vectors,
            ):
                embedded_chunks.append(
                    EmbeddedChunk(
                        id=chunk.id,
                        document_id=chunk.document_id,
                        text=chunk.text,
                        embedding=vector,
                        metadata=chunk.metadata,
                    )
                )

        return embedded_chunks
