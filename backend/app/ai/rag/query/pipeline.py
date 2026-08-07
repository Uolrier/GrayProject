from .base import BaseQueryPipeline
from .schema import (
    QueryRequest,
    QueryResponse,
    QueryResult,
)


class QueryPipeline(BaseQueryPipeline):
    def __init__(
        self,
        retriever,
        reranker=None,
    ):
        self.retriever = retriever
        self.reranker = reranker

    def run(
        self,
        request: QueryRequest,
    ) -> QueryResponse:
        documents = self.retriever.search(
            request.query,
            top_k=request.top_k,
        )

        if self.reranker:
            documents = self.reranker.rank(
                request.query,
                documents,
            )

        results = []

        for doc in documents:
            results.append(
                QueryResult(
                    content=doc.content,
                    score=getattr(
                        doc,
                        "score",
                        0,
                    ),
                    metadata=doc.metadata,
                )
            )

        return QueryResponse(
            query=request.query,
            results=results,
        )
