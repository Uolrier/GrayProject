from backend.app.ai.rag.retrieval.multi_retriever import MultiRetriever
from backend.app.ai.rag.retrieval.schema import RetrievedDocument


class DummyRetriever:
    def __init__(self, name):
        self.name = name

    def search(
        self,
        query,
        top_k=5,
    ):
        return [
            RetrievedDocument(
                id=self.name,
                text=f"{self.name} document",
                score=0.9,
                metadata={},
            )
        ]


def test_multi_retriever_merge():
    retriever = MultiRetriever(
        {
            "code": DummyRetriever("code"),
            "docs": DummyRetriever("docs"),
        }
    )

    results = retriever.search(
        "rag",
    )

    assert len(results) == 2


def test_multi_retriever_metadata():
    retriever = MultiRetriever(
        {
            "code": DummyRetriever("code"),
        }
    )

    results = retriever.search(
        "query",
    )

    assert results[0].metadata["knowledge_base"] == "code"


def test_multi_retriever_top_k():
    retriever = MultiRetriever(
        {
            "code": DummyRetriever("code"),
            "docs": DummyRetriever("docs"),
        }
    )

    results = retriever.search(
        "query",
        top_k=1,
    )

    assert len(results) == 1
