from abc import ABC, abstractmethod

from .schema import SecurityResult


class BaseSecurityFilter(ABC):
    """
    Base interface for security filters.
    """

    name: str = "base"

    @abstractmethod
    def check(self, data) -> SecurityResult:
        """
        Check input data.
        """
        pass

    @abstractmethod
    def filter(self, data):
        """
        Return filtered data.
        """
        pass
