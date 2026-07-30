"""
OpenAI Compatible LLM base implementation.

Provide common logic for all providers exposing an
OpenAI-compatible API.
"""

from typing import Iterator

from openai import OpenAI

from backend.app.llm.base import BaseLLM


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
        self._model_name = model_name

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

    @property
    def model_name(self) -> str:
        return self._model_name

    def generate(self, prompt: str, **kwargs) -> str:
        response = self.client.chat.completions.create(
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
        response = self.client.chat.completions.create(
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
