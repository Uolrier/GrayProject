import os
from typing import Iterator

from openai import OpenAI

from backend.app.llm.base import BaseLLM
from backend.app.llm.registry import register_provider


@register_provider("openai")
class OpenAILLM(BaseLLM):
    """
    OpenAI LLM Provider

    接入 OpenAI API
    """

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

        self._model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

        self.client = None

    @property
    def model_name(self) -> str:
        return self._model_name

    def generate(self, prompt: str, **kwargs) -> str:
        if self.client is None:
            self.client = OpenAI(api_key=self.api_key)
        response = self.client.chat.completions.create(
            model=self._model_name,
            messages=[{"role": "user", "content": prompt}],
            **kwargs,
        )

        return response.choices[0].message.content

    def stream(self, prompt: str, **kwargs) -> Iterator[str]:
        response = self.client.chat.completions.create(
            model=self._model_name,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            **kwargs,
        )

        for chunk in response:
            content = chunk.choices[0].delta.content

            if content:
                yield content
