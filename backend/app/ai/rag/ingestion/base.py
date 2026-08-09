from abc import ABC, abstractmethod
from typing import Iterator, List

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

    def iter_load(self) -> Iterator[Document]:
        """
        Stream documents one by one.

        Supports loaders returning either:
            - Document
            - List[Document]
        """

        result = self.load()

        if isinstance(result, Document):
            yield result
        else:
            yield from result
