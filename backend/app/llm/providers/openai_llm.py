import os

from ..registry import register_provider
from .openai_compatible import OpenAICompatibleLLM


@register_provider("openai")
class OpenAILLM(OpenAICompatibleLLM):
    """
    OpenAI LLM Provider
    """

    def __init__(self):
        super().__init__(
            api_key=os.getenv("OPENAI_API_KEY"),
            model_name=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        )
