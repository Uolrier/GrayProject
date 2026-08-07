from backend.app.ai.rag.query.pipeline import QueryPipeline
from backend.app.ai.rag.query.schema import QueryRequest


class DummyDocument:
    def __init__(self):
        self.page_content = "RAG content"

        self.score = 0.9

        self.metadata = {
            "source": "rag.md",
            "chunk_id": "chunk-1",
        }


class DummyRetriever:
    def search(
        self,
        query,
        top_k=5,
    ):
        return [
            DummyDocument(),
        ]


class DummySecurityManager:
    def filter_documents(
        self,
        documents,
    ):
        return documents


def test_query_pipeline_sources():
    pipeline = QueryPipeline(
        retriever=DummyRetriever(),
        security_manager=DummySecurityManager(),
    )

    request = QueryRequest(
        query="what is RAG?",
    )

    response = pipeline.run(
        request,
    )

    assert len(response.sources) == 1

    assert response.sources[0].file_path == "rag.md"

    assert response.sources[0].chunk_id == "chunk-1"

    assert response.sources[0].score == 0.9
