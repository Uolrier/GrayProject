from .base import BaseQueryCache
from .memory import MemoryQueryCache


class QueryCacheFactory:
    """Factory for query cache implementations."""

    @staticmethod
    def create(cache_type: str = "memory") -> BaseQueryCache:
        if cache_type == "memory":
            return MemoryQueryCache()

        raise ValueError(f"Unsupported query cache type: {cache_type}")
