from abc import ABC, abstractmethod
from collections.abc import Generator

from .schema import ChatRequest, ChatResponse
from .stream import StreamChunk


class BaseLLM(ABC):
    """
    GrayProject LLM 基础抽象接口

    所有 LLM 实现必须继承该类
    """

    @property
    @abstractmethod
    def model_name(self) -> str:
        """
        当前模型名称
        """
        pass

    @abstractmethod
    def chat(self, request: ChatRequest) -> ChatResponse:
        """
        Chat接口

        Args:
            request:
                LLM聊天请求协议

        Returns:
            LLM聊天响应协议
        """
        pass

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
    def stream(
        self,
        prompt: str | None = None,
        messages=None,
        **kwargs,
    ) -> Generator[StreamChunk, None, None]:
        """
        流式生成。

        Args:
            prompt:
                输入文本。

        Yields:
            StreamChunk:
                模型生成的流式输出片段。
        """
        pass
