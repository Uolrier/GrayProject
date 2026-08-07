from .factory import KnowledgeBaseFactory
from .schema import KnowledgeBaseConfig


class KnowledgeBaseManager:
    """
    Knowledge base manager.

    Responsible for:
    - creating knowledge bases
    - storing instances
    - retrieving instances
    """

    def __init__(self):
        self._knowledge_bases = {}

    def create(
        self,
        config: KnowledgeBaseConfig,
    ):
        """
        Create and register a knowledge base.
        """

        if config.name in self._knowledge_bases:
            raise ValueError(f"Knowledge base already exists: {config.name}")

        knowledge_base = KnowledgeBaseFactory.create(config)

        if config.auto_update:
            knowledge_base.enable_auto_update()

        self._knowledge_bases[config.name] = knowledge_base

        return knowledge_base

    def get(
        self,
        name: str,
    ):
        """
        Get knowledge base instance.
        """

        if name not in self._knowledge_bases:
            raise KeyError(f"Knowledge base not found: {name}")

        return self._knowledge_bases[name]

    def delete(
        self,
        name: str,
    ):
        """
        Remove knowledge base instance.
        """

        if name not in self._knowledge_bases:
            raise KeyError(f"Knowledge base not found: {name}")

        knowledge_base = self._knowledge_bases.pop(name)

        if hasattr(
            knowledge_base,
            "disable_auto_update",
        ):
            knowledge_base.disable_auto_update()

        knowledge_base.delete()

    def list(
        self,
    ) -> list[str]:
        """
        List managed knowledge bases.
        """

        return list(self._knowledge_bases.keys())

    def clear(
        self,
    ):
        """
        Clear all knowledge bases.
        """

        self._knowledge_bases.clear()
