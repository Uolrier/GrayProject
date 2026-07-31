"""Base embedding interface."""

from abc import ABC, abstractmethod


class BaseEmbedding(ABC):
    """
    GrayProject Embedding 基础抽象接口

    所有 Embedding 实现必须继承该类
    """

    @property
    @abstractmethod
    def model_name(self) -> str:
        """
        当前 embedding 模型名称
        """
        pass

    @abstractmethod
    def embed_text(self, text: str) -> list[float]:
        """
        单文本向量化

        Args:
            text:
                输入文本

        Returns:
            embedding vector
        """
        pass

    @abstractmethod
    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        批量文本向量化

        Args:
            texts:
                输入文本列表

        Returns:
            embedding vectors
        """
        pass
