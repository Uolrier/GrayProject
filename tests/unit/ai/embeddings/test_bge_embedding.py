from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from backend.app.ai.embeddings.providers.bge_embedding import BGEEmbedding


@patch("backend.app.ai.embeddings.providers.bge_embedding.SentenceTransformer")
def test_create_bge_embedding(mock_sentence_transformer):
    mock_sentence_transformer.return_value = MagicMock()

    embedding = BGEEmbedding()

    assert embedding.model_name == "BAAI/bge-small-zh-v1.5"


@patch("backend.app.ai.embeddings.providers.bge_embedding.SentenceTransformer")
def test_embed_text(mock_sentence_transformer):
    model = MagicMock()

    model.encode.return_value = np.array([1.0, 2.0, 3.0])

    mock_sentence_transformer.return_value = model

    embedding = BGEEmbedding()

    vector = embedding.embed_text("hello")

    assert vector == [1.0, 2.0, 3.0]

    model.encode.assert_called_once()


@patch("backend.app.ai.embeddings.providers.bge_embedding.SentenceTransformer")
def test_embed_documents(mock_sentence_transformer):
    model = MagicMock()

    model.encode.return_value = np.array(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    mock_sentence_transformer.return_value = model

    embedding = BGEEmbedding()

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


@patch("backend.app.ai.embeddings.providers.bge_embedding.SentenceTransformer")
def test_init_failed(mock_sentence_transformer):
    mock_sentence_transformer.side_effect = Exception("download failed")

    with pytest.raises(RuntimeError):
        BGEEmbedding()


@patch("backend.app.ai.embeddings.providers.bge_embedding.SentenceTransformer")
def test_embed_failed(mock_sentence_transformer):
    model = MagicMock()

    model.encode.side_effect = Exception("encode failed")

    mock_sentence_transformer.return_value = model

    embedding = BGEEmbedding()

    with pytest.raises(RuntimeError):
        embedding.embed_text("hello")
