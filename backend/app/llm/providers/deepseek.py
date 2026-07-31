from config.settings import settings

from ..registry import register_provider
from .openai_compatible import OpenAICompatibleLLM


@register_provider("deepseek")
class DeepSeekLLM(OpenAICompatibleLLM):
    """
    DeepSeek API LLM Provider
    """

    def __init__(self):
        super().__init__(
            api_key=settings.DEEPSEEK_API_KEY,
            model_name=settings.DEEPSEEK_MODEL,
            base_url="https://api.deepseek.com",
        )
