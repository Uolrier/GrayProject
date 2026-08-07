from typing import Type

from .base import BaseKnowledgeBase


class KnowledgeBaseRegistry:
    """
    Knowledge base registry.
    """

    def __init__(self):
        self._registry: dict[str, Type[BaseKnowledgeBase]] = {}

    def register(
        self,
        name: str,
        knowledge_base: Type[BaseKnowledgeBase],
    ):
        """
        Register a knowledge base implementation.
        """

        if name in self._registry:
            raise ValueError(f"Knowledge base already registered: {name}")

        self._registry[name] = knowledge_base

    def get(
        self,
        name: str,
    ) -> Type[BaseKnowledgeBase]:
        """
        Get knowledge base implementation.
        """

        if name not in self._registry:
            raise KeyError(f"Knowledge base not found: {name}")

        return self._registry[name]

    def contains(
        self,
        name: str,
    ) -> bool:
        """
        Check whether knowledge base exists.
        """

        return name in self._registry

    def list(
        self,
    ) -> list[str]:
        """
        List registered knowledge bases.
        """

        return list(self._registry.keys())

    def clear(
        self,
    ):
        """
        Clear registry.
        """

        self._registry.clear()


knowledge_base_registry = KnowledgeBaseRegistry()
