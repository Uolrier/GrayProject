from abc import ABC, abstractmethod

from .schema import EmbeddingCacheItem


class BaseEmbeddingCache(ABC):
    """
    Embedding cache interface.
    """

    @abstractmethod
    def get(self, key: str) -> EmbeddingCacheItem | None:
        pass

    @abstractmethod
    def set(self, key: str, value: EmbeddingCacheItem) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
