from .base import BaseRetriever
from .schema import RetrievedDocument


class MultiRetriever(BaseRetriever):
    """
    Retriever for multiple knowledge bases.

    Combine results from multiple retrievers.
    """

    def __init__(
        self,
        retrievers: dict[str, BaseRetriever],
    ):
        """
        Args:
            retrievers:
                {
                    "knowledge_base_name":
                        retriever
                }
        """

        self.retrievers = retrievers

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[RetrievedDocument]:
        results = []

        for name, retriever in self.retrievers.items():
            docs = retriever.search(
                query=query,
                top_k=top_k,
            )

            for doc in docs:
                if doc.metadata is None:
                    doc.metadata = {}

                doc.metadata["knowledge_base"] = name

                results.append(doc)

        results.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        return results[:top_k]
