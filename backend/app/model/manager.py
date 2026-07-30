from backend.app.llm.registry import get_provider
from backend.app.runtime.registry import RuntimeRegistry

from .config import load_model_config


class ModelManager:
    """
    Unified model switch manager.
    """

    @staticmethod
    def create(name: str, **kwargs):
        """
        Create model instance.
        """

        try:
            model_cls = get_provider(name)
            return model_cls(**kwargs)

        except ValueError:
            pass

        try:
            model_cls = RuntimeRegistry.get(name)
            return model_cls(**kwargs)

        except ValueError:
            pass

        raise ValueError(f"Model '{name}' is not registered")

    @staticmethod
    def create_active(**kwargs):
        """
        Create active model from config.
        """

        config = load_model_config()

        model_name = config["active_model"]

        return ModelManager.create(
            model_name,
            **kwargs,
        )
