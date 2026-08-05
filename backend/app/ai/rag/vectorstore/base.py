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
