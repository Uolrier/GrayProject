from app.ai.rag.retrieval.vector_retriever import VectorRetriever


class DummyEmbedding:
    def embed_text(self, text):
        return [0.1, 0.2, 0.3]


class DummyVectorStore:
    def query(
        self,
        embedding,
        top_k=5,
    ):
        from app.ai.rag.vectorstore.schema import SearchResult

        return [
            SearchResult(
                id="1", text="RAG document", score=0.9, metadata={"source": "test"}
            )
        ]


def test_vector_retriever():
    retriever = VectorRetriever(
        embedding=DummyEmbedding(),
        vector_store=DummyVectorStore(),
    )

    results = retriever.search("what is RAG?")

    assert len(results) == 1

    assert results[0].text == "RAG document"

    assert results[0].score == 0.9
