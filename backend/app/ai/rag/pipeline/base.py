from abc import ABC, abstractmethod
from typing import Any


class BasePipeline(ABC):
    """
    RAG Pipeline abstract interface.
    """

    @abstractmethod
    def run(self, data: Any):
        """
        Execute pipeline.
        """
        pass
