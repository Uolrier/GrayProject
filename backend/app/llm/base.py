from abc import ABC, abstractmethod
from typing import Iterator


class BaseLLM(ABC):
    """
    GrayProject LLM 基础抽象接口

    所有 LLM 实现必须继承该类
    """

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        非流式生成

        Args:
            prompt:
                输入文本

        Returns:
            模型生成结果
        """
        pass

    @abstractmethod
    def stream(self, prompt: str, **kwargs) -> Iterator[str]:
        """
        流式生成

        Args:
            prompt:
                输入文本

        Yields:
            文本片段
        """
        pass
