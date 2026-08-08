from backend.app.ai.rag.context import ContextChunk
from backend.app.ai.rag.source.builder import SourceBuilder
from backend.app.security.manager import (
    SecurityManager,
)

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
        context_builder=None,
        security_manager=None,
    ):
        self.retriever = retriever
        self.reranker = reranker
        self.context_builder = context_builder
        self.security_manager = security_manager or SecurityManager()
        self.source_builder = SourceBuilder()

    def run(
        self,
        request: QueryRequest,
    ) -> QueryResponse:
        documents = self.retriever.search(
            request.query,
            top_k=request.top_k,
        )

        documents = self.security_manager.filter_documents(documents)

        if self.reranker:
            documents = self.reranker.rank(
                request.query,
                documents,
            )

        sources = self.source_builder.build(documents)

        results = []

        for doc in documents:
            content = getattr(
                doc,
                "page_content",
                getattr(
                    doc,
                    "content",
                    getattr(
                        doc,
                        "text",
                        "",
                    ),
                ),
            )

            results.append(
                QueryResult(
                    content=content,
                    score=getattr(
                        doc,
                        "score",
                        0,
                    ),
                    metadata=doc.metadata,
                )
            )

        context = None

        if self.context_builder:
            chunks = []

            for result in results:
                chunks.append(
                    ContextChunk(
                        content=result.content,
                        metadata=result.metadata,
                    )
                )

            built_context = self.context_builder.build(chunks)

            context = built_context.text

        return QueryResponse(
            query=request.query,
            results=results,
            context=context,
            sources=sources,
        )
