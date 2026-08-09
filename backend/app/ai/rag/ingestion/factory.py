from typing import Type

from backend.app.core.registry import Registry

from .base import BaseDocumentLoader

loader_registry = Registry[Type[BaseDocumentLoader]]()


class LoaderFactory:
    """
    Factory for creating document loaders.

    Loader implementations register themselves
    through this factory.
    """

    @staticmethod
    def register(name: str):
        """
        Register a document loader.

        Example:

            @LoaderFactory.register("text")
            class TextLoader(BaseDocumentLoader):
                ...
        """

        return loader_registry.register(name)

    @staticmethod
    def create(name: str, **kwargs) -> BaseDocumentLoader:
        """
        Create loader instance.

        Supports both loader styles:

        1. Constructor injection

            Loader(path)

        2. Runtime path passing

            Loader()
        """

        loader_cls = loader_registry.get(name)

        try:
            return loader_cls(**kwargs)

        except TypeError:
            return loader_cls()

    @staticmethod
    def list_loaders():
        """
        Return available loader names.
        """

        return loader_registry.list()
