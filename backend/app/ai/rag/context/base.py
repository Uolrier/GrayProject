from abc import ABC, abstractmethod
from typing import List

from .schema import BuiltContext, ContextChunk


class BaseContextBuilder(ABC):
    """
    Context assembly interface.
    """

    @abstractmethod
    def build(
        self,
        chunks: List[ContextChunk],
    ) -> BuiltContext:
        pass
