from typing import Dict

from .schema import Metadata


class MetadataManager:
    def __init__(self):
        self._store: Dict[str, Metadata] = {}

    def add(self, metadata: Metadata):
        self._store[metadata.document_id] = metadata

    def get(self, document_id: str):
        return self._store.get(document_id)

    def update(self, document_id: str, **kwargs):
        metadata = self.get(document_id)

        if metadata is None:
            return None

        for key, value in kwargs.items():
            if hasattr(metadata, key):
                setattr(metadata, key, value)
            else:
                metadata.extra[key] = value

        return metadata

    def delete(self, document_id: str):
        return self._store.pop(document_id, None)

    def clear_collection(
        self,
        collection: str,
    ):
        """
        Remove all metadata belonging to a collection.
        """

        removed = []

        for document_id, metadata in list(self._store.items()):
            if metadata.collection == collection:
                removed.append(document_id)

                del self._store[document_id]

        return removed

    def all(self):
        return list(self._store.values())

    def find_by_source(
        self,
        source: str,
    ):
        """
        Find metadata by document source path.
        """

        for metadata in self._store.values():
            if metadata.source == source:
                return metadata

        return None
