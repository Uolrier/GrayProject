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

    def all(self):
        return list(self._store.values())
