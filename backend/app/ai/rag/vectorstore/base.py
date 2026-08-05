from abc import ABC, abstractmethod


class BaseVectorStore(ABC):
    @abstractmethod
    def add(self, records):
        pass

    @abstractmethod
    def delete(self, ids):
        pass

    @abstractmethod
    def query(self, embedding, top_k=5):
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
