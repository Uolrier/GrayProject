from typing import Dict, Type

"""
Unified Model Registry

Manage all available models.
"""

MODELS: Dict[str, Type] = {}


def register_model(name: str):
    """
    Register a model.

    Example:

        @register_model("deepseek")
        class DeepSeekProvider:
            pass
    """

    def decorator(cls: Type):
        MODELS[name] = cls

        return cls

    return decorator


def get_model(name: str) -> Type:
    """
    Get model class.
    """

    if name not in MODELS:
        raise ValueError(f"Unknown model: {name}")

    return MODELS[name]


def list_models():
    """
    List registered models.
    """

    return list(MODELS.keys())
