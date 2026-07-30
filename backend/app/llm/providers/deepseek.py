from backend.app.config import Config

from ..registry import register_provider
from .openai_compatible import OpenAICompatibleLLM


@register_provider("deepseek")
class DeepSeekLLM(OpenAICompatibleLLM):
    """
    DeepSeek API LLM Provider
    """

    def __init__(self):
        super().__init__(
            api_key=Config.DEEPSEEK_API_KEY,
            model_name=Config.DEEPSEEK_MODEL,
            base_url="https://api.deepseek.com",
        )
