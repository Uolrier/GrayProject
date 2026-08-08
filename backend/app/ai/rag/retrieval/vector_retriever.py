from .base import BaseRetriever
from .schema import RetrievedDocument


class VectorRetriever(BaseRetriever):
    """
    Retriever based on vector similarity search.
    """

    def __init__(
        self,
        embedding,
        vector_store,
    ):
        self.embedding = embedding
        self.vector_store = vector_store

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[RetrievedDocument]:
        vector = self.embedding.embed_text(query)

        results = self.vector_store.query(
            embedding=vector,
            top_k=top_k,
        )

        return [
            RetrievedDocument(
                id=item.id,
                text=item.text,
                score=item.score,
                metadata=item.metadata,
            )
            for item in results
        ]
