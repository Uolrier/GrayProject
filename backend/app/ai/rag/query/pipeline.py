from datetime import datetime

from backend.app.ai.rag.cache.query import (
    BaseQueryCache,
    QueryCacheItem,
    create_query_cache_key,
)
from backend.app.ai.rag.context import ContextChunk
from backend.app.ai.rag.source.builder import SourceBuilder
from backend.app.security.manager import SecurityManager

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
        query_cache: BaseQueryCache | None = None,
    ):
        self.retriever = retriever
        self.reranker = reranker
        self.context_builder = context_builder
        self.security_manager = security_manager or SecurityManager()
        self.source_builder = SourceBuilder()
        self.query_cache = query_cache

    def run(
        self,
        request: QueryRequest,
    ) -> QueryResponse:
        cache_key = None

        if self.query_cache:
            cache_key = create_query_cache_key(request)

            cached = self.query_cache.get(cache_key)

            if cached is not None:
                return cached.response

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

        response = QueryResponse(
            query=request.query,
            results=results,
            context=context,
            sources=sources,
        )

        if self.query_cache and cache_key is not None:
            self.query_cache.set(
                cache_key,
                QueryCacheItem(
                    key=cache_key,
                    response=response,
                    created_at=datetime.now(),
                ),
            )

        return response
