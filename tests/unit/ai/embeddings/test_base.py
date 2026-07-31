"""Tests for BaseEmbedding."""

import pytest

from backend.app.ai.embeddings import BaseEmbedding


def test_base_embedding_cannot_be_instantiated():
    """Abstract class cannot be instantiated."""

    with pytest.raises(TypeError):
        BaseEmbedding()


def test_embedding_subclass_requires_methods():
    """Subclass must implement abstract methods."""

    class DummyEmbedding(BaseEmbedding):
        pass

    with pytest.raises(TypeError):
        DummyEmbedding()


def test_embedding_subclass_can_be_created():
    """Subclass implementing all methods should be instantiable."""

    class DummyEmbedding(BaseEmbedding):
        @property
        def model_name(self) -> str:
            return "dummy"

        def embed_text(self, text: str) -> list[float]:
            return [0.0]

        def embed_documents(self, texts: list[str]) -> list[list[float]]:
            return [[0.0] for _ in texts]

    embedding = DummyEmbedding()

    assert embedding.model_name == "dummy"
    assert embedding.embed_text("hello") == [0.0]
    assert embedding.embed_documents(["a", "b"]) == [[0.0], [0.0]]
