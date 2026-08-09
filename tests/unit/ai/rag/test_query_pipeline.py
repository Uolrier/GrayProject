from app.ai.rag.cache.query import QueryCacheFactory
from app.ai.rag.query.pipeline import QueryPipeline
from app.ai.rag.query.schema import QueryRequest


class DummyDocument:
    def __init__(self):
        self.page_content = "test document"
        self.metadata = {"source": "test.md"}
        self.score = 0.95


class DummyRetriever:
    def search(
        self,
        query,
        top_k,
    ):
        assert query == "hello"
        assert top_k == 5

        return [DummyDocument()]


class DummyReranker:
    def rank(
        self,
        query,
        documents,
    ):
        assert query == "hello"

        return documents


def test_query_pipeline_without_reranker():
    pipeline = QueryPipeline(
        retriever=DummyRetriever(),
    )

    request = QueryRequest(
        query="hello",
    )

    response = pipeline.run(request)

    assert response.query == "hello"

    assert len(response.results) == 1

    assert response.results[0].content == "test document"

    assert response.results[0].score == 0.95


def test_query_pipeline_with_reranker():
    pipeline = QueryPipeline(
        retriever=DummyRetriever(),
        reranker=DummyReranker(),
    )

    request = QueryRequest(
        query="hello",
        top_k=5,
    )

    response = pipeline.run(request)

    assert len(response.results) == 1

    assert response.results[0].metadata["source"] == "test.md"


class CountingRetriever:
    def __init__(self):
        self.calls = 0

    def search(
        self,
        query,
        top_k,
    ):
        self.calls += 1

        return [DummyDocument()]


def test_query_pipeline_cache_hit_avoids_retrieval():
    retriever = CountingRetriever()
    cache = QueryCacheFactory.create()

    pipeline = QueryPipeline(
        retriever=retriever,
        query_cache=cache,
    )

    request = QueryRequest(
        query="hello",
    )

    first_response = pipeline.run(request)
    second_response = pipeline.run(request)

    assert retriever.calls == 1

    assert second_response is first_response
    assert second_response.query == "hello"
    assert len(second_response.results) == 1


def test_query_pipeline_cache_miss_executes_retrieval():
    retriever = CountingRetriever()
    cache = QueryCacheFactory.create()

    pipeline = QueryPipeline(
        retriever=retriever,
        query_cache=cache,
    )

    request = QueryRequest(
        query="hello",
    )

    response = pipeline.run(request)

    assert retriever.calls == 1
    assert response.query == "hello"


def test_query_pipeline_cache_respects_top_k():
    retriever = CountingRetriever()
    cache = QueryCacheFactory.create()

    pipeline = QueryPipeline(
        retriever=retriever,
        query_cache=cache,
    )

    request1 = QueryRequest(
        query="hello",
        top_k=5,
    )

    request2 = QueryRequest(
        query="hello",
        top_k=10,
    )

    pipeline.run(request1)
    pipeline.run(request2)

    assert retriever.calls == 2


def test_query_pipeline_cache_respects_knowledge_base():
    retriever = CountingRetriever()
    cache = QueryCacheFactory.create()

    pipeline = QueryPipeline(
        retriever=retriever,
        query_cache=cache,
    )

    request1 = QueryRequest(
        query="hello",
        knowledge_base="default",
    )

    request2 = QueryRequest(
        query="hello",
        knowledge_base="other",
    )

    pipeline.run(request1)
    pipeline.run(request2)

    assert retriever.calls == 2
