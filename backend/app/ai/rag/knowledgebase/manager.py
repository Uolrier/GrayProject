from .factory import KnowledgeBaseFactory
from .persistence import KnowledgeBasePersistence
from .schema import KnowledgeBaseConfig


class KnowledgeBaseManager:
    """
    Knowledge base manager.

    Responsible for:
    - creating knowledge bases
    - storing instances
    - retrieving instances
    """

    def __init__(
        self,
        persistence: KnowledgeBasePersistence | None = None,
    ):
        self._knowledge_bases = {}
        self.persistence = persistence or KnowledgeBasePersistence()

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

        self.persistence.save(
            [knowledge_base.config for knowledge_base in self._knowledge_bases.values()]
        )

        return knowledge_base

    def load(self):
        """
        Restore persisted knowledge bases.
        """

        configs = self.persistence.load()

        for config in configs:
            if config.name in self._knowledge_bases:
                continue

            knowledge_base = KnowledgeBaseFactory.create(config)

            self._knowledge_bases[config.name] = knowledge_base

            if config.auto_update:
                knowledge_base.enable_auto_update()

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

        knowledge_base.disable_auto_update()
        knowledge_base.delete()

        self.persistence.save(
            [knowledge_base.config for knowledge_base in self._knowledge_bases.values()]
        )

    def list(
        self,
    ) -> list[str]:
        """
        List managed knowledge bases.
        """

        return list(self._knowledge_bases.keys())

    def clear(self):
        """
        Clear all knowledge bases.
        """

        for knowledge_base in self._knowledge_bases.values():
            knowledge_base.disable_auto_update()

        self._knowledge_bases.clear()
