from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from backend.app.ai.embeddings.providers.jina_embedding import JinaEmbedding


@patch("backend.app.ai.embeddings.providers.jina_embedding.SentenceTransformer")
def test_create_jina_embedding(mock_sentence_transformer):
    mock_sentence_transformer.return_value = MagicMock()

    embedding = JinaEmbedding()

    assert embedding.model_name == "jinaai/jina-embeddings-v3"


@patch("backend.app.ai.embeddings.providers.jina_embedding.SentenceTransformer")
def test_embed_text(mock_sentence_transformer):
    model = MagicMock()

    model.encode.return_value = np.array([1.0, 2.0, 3.0])

    mock_sentence_transformer.return_value = model

    embedding = JinaEmbedding()

    vector = embedding.embed_text("hello")

    assert vector == [1.0, 2.0, 3.0]

    model.encode.assert_called_once()


@patch("backend.app.ai.embeddings.providers.jina_embedding.SentenceTransformer")
def test_embed_documents(mock_sentence_transformer):
    model = MagicMock()

    model.encode.return_value = np.array(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    mock_sentence_transformer.return_value = model

    embedding = JinaEmbedding()

    vectors = embedding.embed_documents(
        [
            "hello",
            "world",
        ]
    )

    assert vectors == [
        [1.0, 2.0],
        [3.0, 4.0],
    ]


@patch("backend.app.ai.embeddings.providers.jina_embedding.SentenceTransformer")
def test_init_failed(mock_sentence_transformer):
    mock_sentence_transformer.side_effect = Exception("download failed")

    with pytest.raises(RuntimeError):
        JinaEmbedding()


@patch("backend.app.ai.embeddings.providers.jina_embedding.SentenceTransformer")
def test_embed_failed(mock_sentence_transformer):
    model = MagicMock()

    model.encode.side_effect = Exception("encode failed")

    mock_sentence_transformer.return_value = model

    embedding = JinaEmbedding()

    with pytest.raises(RuntimeError):
        embedding.embed_text("hello")
