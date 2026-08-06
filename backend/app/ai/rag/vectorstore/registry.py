from typing import Optional, Type

from backend.app.core.registry import Registry

from .base import BaseVectorStore

VECTORSTORE_REGISTRY: Registry[Type[BaseVectorStore]] = Registry()


def register_vectorstore(
    name: str,
    store_cls: Optional[Type[BaseVectorStore]] = None,
):
    """
    Register vector store implementation.

    Example:

        @register_vectorstore("chroma")
        class ChromaVectorStore:
            ...
    """

    return VECTORSTORE_REGISTRY.register(
        name,
        store_cls,
    )


def get_vectorstore(
    name: str,
):
    return VECTORSTORE_REGISTRY.get(name)


def list_vectorstores():
    return VECTORSTORE_REGISTRY.list()
