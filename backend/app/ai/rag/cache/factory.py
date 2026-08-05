from .base import BaseEmbeddingCache
from .memory import MemoryEmbeddingCache


class EmbeddingCacheFactory:
    """
    Embedding cache factory.
    """

    @staticmethod
    def create(cache_type: str = "memory") -> BaseEmbeddingCache:
        if cache_type == "memory":
            return MemoryEmbeddingCache()

        raise ValueError(f"Unsupported embedding cache type: {cache_type}")
