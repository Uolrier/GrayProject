from typing import Dict, Type

from .base import BaseLLM


class LLMFactory:
    """
    Factory for creating LLM instances.
    """

    _providers: Dict[str, Type[BaseLLM]] = {}

    @classmethod
    def register(cls, name: str, llm_class: Type[BaseLLM]):
        """
        Register an LLM provider.
        """
        cls._providers[name] = llm_class

    @classmethod
    def create(cls, provider: str, **kwargs) -> BaseLLM:
        """
        Create an LLM instance by provider name.
        """

        if provider not in cls._providers:
            raise ValueError(f"Unsupported LLM provider: {provider}")

        llm_class = cls._providers[provider]

        return llm_class(**kwargs)
