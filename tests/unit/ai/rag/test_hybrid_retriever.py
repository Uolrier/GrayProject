from app.ai.rag.retrieval.hybrid_retriever import (
    HybridRetriever,
)
from app.ai.rag.retrieval.schema import (
    RetrievedDocument,
)


class DummyRetriever:
    def __init__(self, docs):
        self.docs = docs

    def search(
        self,
        query,
        top_k=5,
    ):
        return self.docs[:top_k]


def test_hybrid_dense_only():
    dense = DummyRetriever(
        [
            RetrievedDocument(
                id="1",
                text="dense result",
                score=0.8,
                metadata={},
            )
        ]
    )

    retriever = HybridRetriever(
        dense_retriever=dense,
    )

    results = retriever.search(
        "test",
    )

    assert len(results) == 1
    assert results[0].id == "1"


def test_hybrid_merge():
    dense = DummyRetriever(
        [
            RetrievedDocument(
                id="1",
                text="same",
                score=0.8,
                metadata={},
            )
        ]
    )

    sparse = DummyRetriever(
        [
            RetrievedDocument(
                id="1",
                text="same",
                score=0.6,
                metadata={},
            ),
            RetrievedDocument(
                id="2",
                text="sparse",
                score=0.9,
                metadata={},
            ),
        ]
    )

    retriever = HybridRetriever(
        dense_retriever=dense,
        sparse_retriever=sparse,
    )

    results = retriever.search(
        "test",
    )

    assert len(results) == 2

    assert results[0].id == "1"

    assert results[0].score > 0.7
