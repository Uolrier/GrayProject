"""
Unified BaseRegistry for GrayProject.

Consolidates the previously duplicated registry logic from:
- backend/app/llm/registry.py (function-style)
- backend/app/runtime/registry.py (class-style)
- backend/app/model/registry.py (function-style)

All modules can now use or subclass this single implementation.
"""

from typing import Dict, Generic, Optional, TypeVar

T = TypeVar("T")


class Registry(Generic[T]):
    """
    A generic, reusable registry for managing named class/object lookups.

    Usage (class-style):
        llm_registry = Registry[BaseLLM]()
        llm_registry.register("openai", OpenAILLM)
        llm_registry.get("openai")

    Usage (decorator-style):
        @provider_registry.register("deepseek")
        class DeepSeekLLM(BaseLLM):
            pass
    """

    def __init__(self):
        self._items: Dict[str, T] = {}

    def register(self, name: str, item: Optional[T] = None):
        """
        Register a named item.

        Supports both direct registration and decorator usage.

        Direct:
            registry.register("openai", OpenAILLM)

        Decorator:
            @registry.register("deepseek")
            class DeepSeekLLM(BaseLLM):
                pass
        """
        if item is not None:
            self._items[name] = item
            return item

        def decorator(cls: T) -> T:
            self._items[name] = cls
            return cls

        return decorator

    def get(self, name: str) -> T:
        """
        Get registered item by name.

        Raises ValueError if name is not registered.
        """
        if name not in self._items:
            raise ValueError(f"Unknown '{name}'. Available: {list(self._items.keys())}")
        return self._items[name]

    def list(self) -> list:
        """List all registered names."""
        return list(self._items.keys())
