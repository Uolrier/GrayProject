"""Runtime registry (uses unified Registry from core)."""

from typing import Optional, Type

from ..core.registry import Registry
from .base import BaseRuntime

RUNTIME_REGISTRY: Registry[Type[BaseRuntime]] = Registry()


def register_runtime(name: str, runtime_cls: Optional[Type[BaseRuntime]] = None):
    """Register a runtime class. Supports both direct and decorator usage."""
    return RUNTIME_REGISTRY.register(name, runtime_cls)


def get_runtime(name: str) -> Type[BaseRuntime]:
    """Get a registered runtime class by name."""
    return RUNTIME_REGISTRY.get(name)


def list_runtimes() -> list:
    """List all registered runtime names."""
    return RUNTIME_REGISTRY.list()
