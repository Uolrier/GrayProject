from app.ai.rag.context import (
    SimpleContextBuilder,
)
from app.ai.rag.query import (
    QueryPipeline,
    QueryRequest,
)


class DummyRetriever:
    def search(
        self,
        query,
        top_k,
    ):
        class Doc:
            page_content = "hello rag"

            metadata = {"source": "test.md"}

        return [Doc()]


def test_query_pipeline_context():
    pipeline = QueryPipeline(
        retriever=DummyRetriever(),
        context_builder=SimpleContextBuilder(),
    )

    response = pipeline.run(QueryRequest(query="test"))

    assert response.context

    assert "hello rag" in response.context
