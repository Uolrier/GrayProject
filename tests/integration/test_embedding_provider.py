import pytest

from backend.app.ai.embeddings.registry import get_embedding


@pytest.mark.integration
def test_bge_embedding_registered():
    embedding = get_embedding("bge")

    assert embedding is not None
    assert embedding.__name__ == "BGEEmbedding"


@pytest.mark.integration
def test_jina_embedding_registered():
    embedding = get_embedding("jina")

    assert embedding is not None
    assert embedding.__name__ == "JinaEmbedding"


@pytest.mark.integration
def test_openai_embedding_registered():
    embedding = get_embedding("openai")

    assert embedding is not None
    assert embedding.__name__ == "OpenAIEmbedding"
