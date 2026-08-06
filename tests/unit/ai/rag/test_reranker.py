from app.ai.rag.reranking import RerankerFactory
from app.ai.rag.reranking.schema import (
    RerankDocument,
    RerankRequest,
)


def test_dummy_reranker():
    reranker = RerankerFactory.create("dummy")

    request = RerankRequest(
        query="python",
        documents=[
            RerankDocument(
                id="1",
                text="python code",
            ),
            RerankDocument(
                id="2",
                text="java code",
            ),
        ],
        top_k=1,
    )

    result = reranker.rerank(request)

    assert len(result.items) == 1
    assert result.items[0].id == "1"


def test_registry():
    reranker = RerankerFactory.create("dummy")

    assert reranker.name == "dummy"
