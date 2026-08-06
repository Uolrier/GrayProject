from .base import BaseRetriever
from .schema import RetrievedDocument


class HybridRetriever(BaseRetriever):
    """
    Hybrid retriever.

    Combine dense retrieval and sparse retrieval.

    Dense retrieval:
        Vector similarity search.

    Sparse retrieval:
        Reserved for future BM25 / keyword search.

    Current implementation:
        Dense retrieval only with extension point.
    """

    def __init__(
        self,
        dense_retriever: BaseRetriever,
        sparse_retriever: BaseRetriever | None = None,
        dense_weight: float = 0.7,
        sparse_weight: float = 0.3,
    ):
        self.dense_retriever = dense_retriever
        self.sparse_retriever = sparse_retriever

        self.dense_weight = dense_weight
        self.sparse_weight = sparse_weight

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[RetrievedDocument]:
        """
        Hybrid search.

        Currently:
            dense retrieval result is returned.

        Future:
            merge dense + sparse results.
        """

        dense_results = self.dense_retriever.search(
            query=query,
            top_k=top_k,
        )

        if self.sparse_retriever is None:
            return dense_results

        sparse_results = self.sparse_retriever.search(
            query=query,
            top_k=top_k,
        )

        return self._merge_results(
            dense_results,
            sparse_results,
            top_k,
        )

    def _merge_results(
        self,
        dense_results: list[RetrievedDocument],
        sparse_results: list[RetrievedDocument],
        top_k: int,
    ) -> list[RetrievedDocument]:
        """
        Merge dense and sparse results.

        Placeholder implementation.

        Future:
            - score normalization
            - RRF
            - weighted fusion
        """

        result_map = {}

        for doc in dense_results:
            result_map[doc.id] = RetrievedDocument(
                id=doc.id,
                text=doc.text,
                score=doc.score * self.dense_weight,
                metadata=doc.metadata,
            )

        for doc in sparse_results:
            if doc.id in result_map:
                result_map[doc.id].score += doc.score * self.sparse_weight

            else:
                result_map[doc.id] = RetrievedDocument(
                    id=doc.id,
                    text=doc.text,
                    score=(doc.score * self.sparse_weight),
                    metadata=doc.metadata,
                )

        results = list(result_map.values())

        results.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        return results[:top_k]
