import os

from backend.app.llm.providers.openai_compatible import OpenAICompatibleLLM
from backend.app.llm.registry import register_provider


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
