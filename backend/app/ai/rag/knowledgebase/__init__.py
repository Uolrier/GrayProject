from .providers.local import LocalKnowledgeBase
from .registry import knowledge_base_registry

knowledge_base_registry.register(
    "local",
    LocalKnowledgeBase,
)


__all__ = [
    "LocalKnowledgeBase",
]
