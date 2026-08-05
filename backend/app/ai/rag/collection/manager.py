from .registry import CollectionRegistry
from .schema import CollectionInfo


class CollectionManager:
    def __init__(self, vectorstore=None, registry=None):
        self.vectorstore = vectorstore

        self.registry = registry or CollectionRegistry()

    def create(
        self,
        name: str,
        description=None,
        metadata=None,
    ):
        existing = self.registry.get(name)

        if existing:
            return existing

        if self.vectorstore:
            self.vectorstore.create_collection(name)

        collection = CollectionInfo(
            name=name,
            description=description,
            metadata=metadata or {},
        )

        self.registry.register(collection)

        return collection

    def get(self, name: str) -> CollectionInfo | None:
        return self.registry.get(name)

    def delete(self, name: str):
        if self.vectorstore:
            self.vectorstore.delete_collection(name)

        return self.registry.remove(name)

    def list(self) -> list[CollectionInfo]:
        return self.registry.list()
