from backend.app.ai.rag.retrieval.vector_retriever import VectorRetriever
from backend.app.ai.rag.vectorstore.schema import SearchResult


class DummyEmbedding:
    def embed_text(self, text):
        return [0.1, 0.2, 0.3]


class DummyVectorStore:
    def __init__(self):
        self.received_top_k = None

    def query(
        self,
        embedding,
        top_k=5,
    ):
        self.received_top_k = top_k

        return [
            SearchResult(
                id="1",
                text="doc1",
                score=0.95,
                metadata={"source": "a"},
            ),
            SearchResult(
                id="2",
                text="doc2",
                score=0.80,
                metadata={"source": "b"},
            ),
            SearchResult(
                id="3",
                text="doc3",
                score=0.60,
                metadata={"source": "c"},
            ),
        ][:top_k]


def test_top_k_limit():
    store = DummyVectorStore()

    retriever = VectorRetriever(
        embedding=DummyEmbedding(),
        vector_store=store,
    )

    results = retriever.search(
        "test query",
        top_k=2,
    )

    assert store.received_top_k == 2

    assert len(results) == 2


def test_retrieval_score_order():
    retriever = VectorRetriever(
        embedding=DummyEmbedding(),
        vector_store=DummyVectorStore(),
    )

    results = retriever.search(
        "test query",
        top_k=3,
    )

    scores = [item.score for item in results]

    assert scores == [
        0.95,
        0.80,
        0.60,
    ]


def test_metadata_preserved():
    retriever = VectorRetriever(
        embedding=DummyEmbedding(),
        vector_store=DummyVectorStore(),
    )

    result = retriever.search("test query")[0]

    assert result.metadata["source"] == "a"
