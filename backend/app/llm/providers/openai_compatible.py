"""
OpenAI Compatible LLM base implementation.

Provide common logic for all providers exposing an
OpenAI-compatible API.
"""

from typing import Iterator

from openai import OpenAI

from ..base import BaseLLM
from ..schema import ChatRequest, ChatResponse, TokenUsage


class OpenAICompatibleLLM(BaseLLM):
    """
    OpenAI Compatible Provider Base Class

    所有兼容 OpenAI API 的 Provider
    都应继承该类。
    """

    def __init__(
        self,
        *,
        api_key: str,
        model_name: str,
        base_url: str | None = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self._model_name = model_name

        self.client = None

    def _get_client(self) -> OpenAI:
        """
        Lazy initialize OpenAI client.
        """

        if self.client is None:
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
            )

        return self.client

    @property
    def model_name(self) -> str:
        return self._model_name

    def chat(self, request: ChatRequest) -> ChatResponse:
        """
        Chat completion interface.
        """

        client = self._get_client()

        messages = []

        if request.system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": request.system_prompt,
                }
            )

        messages.extend(
            [
                {
                    "role": msg.role,
                    "content": msg.content,
                }
                for msg in request.messages
            ]
        )

        response = client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            stream=False,
        )

        usage = None

        if response.usage:
            usage = TokenUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            )

        return ChatResponse(
            content=response.choices[0].message.content,
            model=response.model,
            provider=self.__class__.__name__,
            usage=usage,
        )

    def generate(self, prompt: str, **kwargs) -> str:
        client = self._get_client()

        response = client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            **kwargs,
        )

        return response.choices[0].message.content

    def stream(self, prompt: str, **kwargs) -> Iterator[str]:
        client = self._get_client()

        response = client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            stream=True,
            **kwargs,
        )

        for chunk in response:
            content = chunk.choices[0].delta.content

            if content:
                yield content
