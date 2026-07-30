"""
OpenAI Compatible LLM base implementation.

Provide common logic for all providers exposing an
OpenAI-compatible API.
"""

from typing import Iterator

from openai import OpenAI

from ..base import BaseLLM


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
