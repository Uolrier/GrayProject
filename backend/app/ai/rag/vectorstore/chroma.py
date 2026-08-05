import chromadb

from .base import BaseVectorStore
from .schema import SearchResult


class ChromaVectorStore(BaseVectorStore):
    def __init__(
        self,
        persist_dir="data/chroma",
        collection_name="grayproject",
    ):
        self.client = chromadb.PersistentClient(path=persist_dir)

        self.collection_name = collection_name

        self.collection = self.client.get_or_create_collection(name=collection_name)

    def create_collection(self, name: str):
        return self.client.get_or_create_collection(name=name)

    def use_collection(self, name: str):
        self.collection = self.client.get_or_create_collection(name=name)

        self.collection_name = name

        return self.collection

    def delete_collection(self, name: str):
        self.client.delete_collection(name=name)

    def list_collections(self):
        return self.client.list_collections()

    def add(self, records):
        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for r in records:
            ids.append(r.id)
            documents.append(r.text)
            embeddings.append(r.embedding)
            metadatas.append(r.metadata)

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def delete(self, ids):
        self.collection.delete(ids=ids)

    def query(self, embedding, top_k=5):
        result = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        output = []

        for i in range(len(result["ids"][0])):
            output.append(
                SearchResult(
                    id=result["ids"][0][i],
                    text=result["documents"][0][i],
                    score=result["distances"][0][i],
                    metadata=result["metadatas"][0][i],
                )
            )

        return output

    def count(self):
        return self.collection.count()
