from backend.app.runtime.registry import get_runtime
from config.settings import load_model_config

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


class ModelManager:
    """
    Unified model switch manager.

    Tries LLM providers first (API-based), then falls back to
    local runtimes (HuggingFace, etc.).
    """

    @staticmethod
    def create(name: str, **kwargs):
        """Create model instance by name."""
        try:
            model_cls = get_provider(name)
            return model_cls(**kwargs)
        except ValueError:
            pass

        try:
            model_cls = get_runtime(name)
            return model_cls(**kwargs)
        except ValueError:
            pass

        raise ValueError(f"Model '{name}' is not registered")

    @staticmethod
    def create_active(**kwargs):
        """Create active model from config."""
        config = load_model_config()
        model_name = config["active_model"]
        return ModelManager.create(model_name, **kwargs)
