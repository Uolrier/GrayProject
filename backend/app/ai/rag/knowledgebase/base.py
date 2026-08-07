from abc import ABC, abstractmethod

from .schema import KnowledgeBaseSearchResult


class BaseKnowledgeBase(ABC):
    """
    Knowledge Base interface.
    """

    @abstractmethod
    def add(
        self,
        path: str,
    ):
        """
        Add documents into knowledge base.
        """

        pass

    @abstractmethod
    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[KnowledgeBaseSearchResult]:
        """
        Search documents from knowledge base.
        """

        pass

    @abstractmethod
    def delete(
        self,
    ):
        """
        Delete knowledge base.
        """

        pass

    @abstractmethod
    def rebuild(
        self,
    ):
        """
        Rebuild knowledge base index.
        """

        pass
