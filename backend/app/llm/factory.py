from .base import BaseLLM
from .registry import get_provider


class LLMFactory:
    """
    Factory for creating LLM instances.
    """

    @classmethod
    def create(cls, provider: str, **kwargs) -> BaseLLM:
        """
        Create an LLM instance by provider name.
        """

        llm_class = get_provider(provider)

        return llm_class(**kwargs)
