from abc import ABC, abstractmethod
from typing import List

from .schema import Document


class BaseDocumentLoader(ABC):
    """
    Abstract interface for document loaders.

    Every loader should convert external data
    into unified Document objects.
    """

    @abstractmethod
    def load(self) -> List[Document]:
        """
        Load documents.

        Returns:
            List[Document]
        """
        pass
