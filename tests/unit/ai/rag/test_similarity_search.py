from backend.app.ai.rag.retrieval.vector_retriever import VectorRetriever


class DummyEmbedding:
    def embed_text(self, text):
        return [0.1, 0.2, 0.3]


class DummyStore:
    def query(self, embedding, top_k):
        from backend.app.ai.rag.vectorstore.schema import SearchResult

        return [
            SearchResult(id="1", text="hello", score=0.9, metadata={}),
            SearchResult(id="2", text="world", score=0.8, metadata={}),
        ]


def test_similarity_search():
    retriever = VectorRetriever(
        embedding=DummyEmbedding(),
        vector_store=DummyStore(),
    )

    results = retriever.search("hello", top_k=2)

    assert len(results) == 2

    assert results[0].score > results[1].score
