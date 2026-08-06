from abc import ABC, abstractmethod

from .schema import RerankRequest, RerankResult


class BaseReranker(ABC):
    """
    Base interface for document reranking.
    """

    name: str = "base"

    @abstractmethod
    def rerank(
        self,
        request: RerankRequest,
    ) -> RerankResult:
        """
        Reorder retrieved documents according to relevance.
        """
        pass
