from backend.app.ai.embeddings.registry import list_embeddings


def test_embedding_registry():
    embeddings = list_embeddings()

    assert "bge" in embeddings
    assert "jina" in embeddings
    assert "openai" in embeddings
