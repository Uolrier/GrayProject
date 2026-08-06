from abc import ABC, abstractmethod


class BaseVectorStore(ABC):
    @abstractmethod
    def add(self, records):
        pass

    @abstractmethod
    def delete(self, ids):
        pass

    @abstractmethod
    def query(
        self,
        embedding,
        top_k=5,
        filters=None,
    ):
        """
        Similarity search.

        Supports metadata filtering.

        Returns results ordered by similarity score.
        Higher score means more similar.
        """
        pass

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def create_collection(self, name: str):
        pass

    @abstractmethod
    def delete_collection(self, name: str):
        pass

    @abstractmethod
    def list_collections(self):
        pass

    @abstractmethod
    def use_collection(self, name: str):
        pass
