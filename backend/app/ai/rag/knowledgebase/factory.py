from .registry import knowledge_base_registry
from .schema import KnowledgeBaseConfig


class KnowledgeBaseFactory:
    """
    Knowledge base factory.
    """

    @staticmethod
    def create(
        config: KnowledgeBaseConfig,
    ):
        """
        Create knowledge base instance.
        """

        knowledge_base_cls = knowledge_base_registry.get(config.type)

        return knowledge_base_cls(
            config=config,
        )
