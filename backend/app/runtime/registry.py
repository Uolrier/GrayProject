from typing import Dict, Type

from .base import BaseRuntime


class RuntimeRegistry:
    """
    Registry for local inference runtimes.
    """

    _runtimes: Dict[str, Type[BaseRuntime]] = {}

    @classmethod
    def register(
        cls,
        name: str,
        runtime_cls: Type[BaseRuntime],
    ):
        """
        Register a runtime implementation.
        """
        cls._runtimes[name] = runtime_cls

    @classmethod
    def get(
        cls,
        name: str,
    ) -> Type[BaseRuntime]:
        """
        Get runtime class by name.
        """
        if name not in cls._runtimes:
            raise ValueError(f"Runtime '{name}' is not registered")

        return cls._runtimes[name]

    @classmethod
    def list(cls):
        """
        List available runtimes.
        """
        return list(cls._runtimes.keys())
