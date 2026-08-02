from ..registry import register_provider
from .openai_compatible import OpenAICompatibleLLM


@register_provider("deepseek")
class DeepSeekLLM(OpenAICompatibleLLM):
    """
    DeepSeek API LLM Provider
    """

    def __init__(self, config: dict, **kwargs):
        super().__init__(
            api_key=config.get("api_key"),
            model_name=config.get(
                "model",
                "deepseek-chat",
            ),
            base_url=config.get(
                "base_url",
                "https://api.deepseek.com",
            ),
            **kwargs,
        )
