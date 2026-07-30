"""LLM provider registry (uses unified Registry from core)."""

from typing import Type

from backend.app.core.registry import Registry
from backend.app.llm.base import BaseLLM

PROVIDER_REGISTRY: Registry[Type[BaseLLM]] = Registry()


def register_provider(name: str):
    """Register a provider class (decorator style)."""
    return PROVIDER_REGISTRY.register(name)


def get_provider(name: str) -> Type[BaseLLM]:
    """Get a registered provider class by name."""
    return PROVIDER_REGISTRY.get(name)
