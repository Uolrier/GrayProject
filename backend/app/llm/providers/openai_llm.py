import os

from ..registry import register_provider
from .openai_compatible import OpenAICompatibleLLM


@register_provider("openai")
class OpenAILLM(OpenAICompatibleLLM):
    """
    OpenAI LLM Provider
    """

    def __init__(
        self,
        config: dict | None = None,
        **kwargs,
    ):
        config = config or {}

        super().__init__(
            api_key=config.get(
                "api_key",
                os.getenv("OPENAI_API_KEY"),
            ),
            model_name=config.get(
                "model",
                os.getenv(
                    "OPENAI_MODEL",
                    "gpt-4.1-mini",
                ),
            ),
            **kwargs,
        )
