"""Embedding registry."""

from typing import Optional, Type

from backend.app.core.registry import Registry

from .base import BaseEmbedding

EMBEDDING_REGISTRY: Registry[Type[BaseEmbedding]] = Registry()


def register_embedding(
    name: str,
    embedding_cls: Optional[Type[BaseEmbedding]] = None,
):
    """
    Register embedding provider.

    Supports:
        @register_embedding("bge")

    or:

        register_embedding("bge", BGEEmbedding)
    """
    return EMBEDDING_REGISTRY.register(
        name,
        embedding_cls,
    )


def get_embedding(
    name: str,
) -> Type[BaseEmbedding]:
    """
    Get embedding provider class.
    """
    return EMBEDDING_REGISTRY.get(name)


def list_embeddings() -> list:
    """
    List registered embeddings.
    """
    return EMBEDDING_REGISTRY.list()
