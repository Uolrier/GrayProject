from datetime import datetime
from typing import List

from backend.app.ai.rag.cache import (
    BaseEmbeddingCache,
    EmbeddingCacheItem,
    create_embedding_cache_key,
)

from .batch import batch_split
from .schema import DocumentChunk, EmbeddedChunk


class EmbeddingPipeline:
    """
    Convert document chunks into embedded chunks.
    """

    def __init__(
        self,
        embedding,
        cache: BaseEmbeddingCache | None = None,
    ):
        self.embedding = embedding
        self.cache = cache

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
            vectors = self._embed_batch(batch)

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

    def _embed_batch(
        self,
        chunks: list[DocumentChunk],
    ) -> list[list[float]]:
        texts = [chunk.text for chunk in chunks]

        # no cache mode
        if self.cache is None:
            return self.embedding.embed_documents(texts)

        vectors: list[list[float] | None] = [None for _ in texts]

        missing_texts = []

        missing_indexes = []

        for index, text in enumerate(texts):
            key = create_embedding_cache_key(
                text,
                self.embedding.model_name,
            )

            cached = self.cache.get(key)

            if cached:
                vectors[index] = cached.vector

            else:
                missing_texts.append(text)

                missing_indexes.append(index)

        if missing_texts:
            new_vectors = self.embedding.embed_documents(missing_texts)

            for index, vector, text in zip(
                missing_indexes,
                new_vectors,
                missing_texts,
            ):
                key = create_embedding_cache_key(
                    text,
                    self.embedding.model_name,
                )

                self.cache.set(
                    key,
                    EmbeddingCacheItem(
                        key=key,
                        vector=vector,
                        model=self.embedding.model_name,
                        created_at=datetime.now(),
                    ),
                )

                vectors[index] = vector

        return vectors
