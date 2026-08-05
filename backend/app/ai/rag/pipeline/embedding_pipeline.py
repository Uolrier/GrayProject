from typing import List

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
    ) -> List[EmbeddedChunk]:
        texts = [chunk.text for chunk in chunks]

        vectors = self.embedding.embed(texts)

        embedded_chunks = []

        for chunk, vector in zip(chunks, vectors):
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
