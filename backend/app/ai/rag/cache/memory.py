from .base import BaseEmbeddingCache
from .schema import EmbeddingCacheItem


class MemoryEmbeddingCache(BaseEmbeddingCache):
    """
    In-memory embedding cache implementation.
    """

    def __init__(self):
        self._cache: dict[str, EmbeddingCacheItem] = {}

    def get(self, key: str) -> EmbeddingCacheItem | None:
        return self._cache.get(key)

    def set(self, key: str, value: EmbeddingCacheItem) -> None:
        self._cache[key] = value

    def clear(self) -> None:
        self._cache.clear()
