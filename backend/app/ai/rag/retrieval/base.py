from abc import ABC, abstractmethod

from .schema import RetrievedDocument


class BaseRetriever(ABC):
    """
    Retriever interface.
    """

    @abstractmethod
    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[RetrievedDocument]:
        """
        Retrieve documents by query.
        """

        pass
