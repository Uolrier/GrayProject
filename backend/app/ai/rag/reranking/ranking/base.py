from abc import ABC, abstractmethod


class RankingStrategy(ABC):
    """
    Base interface for ranking strategies.
    """

    @abstractmethod
    def rank(self, documents):
        """
        Apply ranking strategy.

        Args:
            documents:
                List of RankedDocument

        Returns:
            Ranked documents
        """

        raise NotImplementedError
