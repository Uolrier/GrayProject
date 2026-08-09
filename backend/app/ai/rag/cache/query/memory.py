from .base import BaseQueryCache
from .schema import QueryCacheItem


class MemoryQueryCache(BaseQueryCache):
    """In-memory query result cache."""

    def __init__(self):
        self._cache: dict[str, QueryCacheItem] = {}

    def get(self, key: str) -> QueryCacheItem | None:
        return self._cache.get(key)

    def set(self, key: str, value: QueryCacheItem) -> None:
        self._cache[key] = value

    def delete(self, key: str) -> None:
        self._cache.pop(key, None)

    def clear(self) -> None:
        self._cache.clear()
