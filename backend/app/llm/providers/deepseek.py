from typing import Iterator

from openai import OpenAI

from backend.app.config import Config
from backend.app.llm.base import BaseLLM
from backend.app.llm.registry import register_provider


@register_provider("deepseek")
class DeepSeekLLM(BaseLLM):
    """
    DeepSeek API LLM Provider
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=Config.DEEPSEEK_API_KEY,
            base_url="https://api.deepseek.com",
        )

    @property
    def model_name(self) -> str:
        return Config.DEEPSEEK_MODEL

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
