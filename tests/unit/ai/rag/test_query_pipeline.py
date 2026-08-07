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
