from .schema import CollectionInfo


class CollectionRegistry:
    """
    In-memory collection registry.

    Responsible for tracking collection metadata.
    """

    def __init__(self):
        self._collections: dict[str, CollectionInfo] = {}

    def register(self, collection: CollectionInfo):
        self._collections[collection.name] = collection

    def get(self, name: str) -> CollectionInfo | None:
        return self._collections.get(name)

    def remove(self, name: str) -> CollectionInfo | None:
        return self._collections.pop(name, None)

    def list(self) -> list[CollectionInfo]:
        return list(self._collections.values())
