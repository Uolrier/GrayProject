from abc import ABC, abstractmethod

from .schema import QueryCacheItem


class BaseQueryCache(ABC):
    """Query result cache interface."""

    @abstractmethod
    def get(self, key: str) -> QueryCacheItem | None:
        pass

    @abstractmethod
    def set(self, key: str, value: QueryCacheItem) -> None:
        pass

    @abstractmethod
    def delete(self, key: str) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
