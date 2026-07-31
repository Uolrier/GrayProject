from unittest.mock import MagicMock, patch

from backend.app.ai.embeddings.providers.openai_embedding import (
    OpenAIEmbedding,
)


@patch("backend.app.ai.embeddings.providers.openai_embedding.OpenAI")
def test_openai_embedding_model_name(mock_openai):
    """
    Test default embedding model name.
    """

    embedding = OpenAIEmbedding()

    assert embedding.model_name == "text-embedding-3-small"


@patch("backend.app.ai.embeddings.providers.openai_embedding.OpenAI")
def test_embed_query(mock_openai):
    """
    Test single text embedding.
    """

    mock_client = MagicMock()

    mock_client.embeddings.create.return_value.data = [
        MagicMock(embedding=[0.1, 0.2, 0.3])
    ]

    mock_openai.return_value = mock_client

    embedding = OpenAIEmbedding()

    result = embedding.embed_query("GrayProject")

    assert result == [
        0.1,
        0.2,
        0.3,
    ]

    mock_client.embeddings.create.assert_called_once()


@patch("backend.app.ai.embeddings.providers.openai_embedding.OpenAI")
def test_embed_documents(mock_openai):
    """
    Test batch document embedding.
    """

    mock_client = MagicMock()

    mock_client.embeddings.create.return_value.data = [
        MagicMock(embedding=[0.1, 0.2]),
        MagicMock(embedding=[0.3, 0.4]),
    ]

    mock_openai.return_value = mock_client

    embedding = OpenAIEmbedding()

    result = embedding.embed_documents(
        [
            "Python",
            "AI",
        ]
    )

    assert result == [
        [0.1, 0.2],
        [0.3, 0.4],
    ]

    mock_client.embeddings.create.assert_called_once()


@patch("backend.app.ai.embeddings.providers.openai_embedding.OpenAI")
def test_embed_text(mock_openai):
    mock_client = MagicMock()

    mock_client.embeddings.create.return_value.data = [MagicMock(embedding=[0.1, 0.2])]

    mock_openai.return_value = mock_client

    embedding = OpenAIEmbedding()

    result = embedding.embed_text("GrayProject")

    assert result == [
        0.1,
        0.2,
    ]

    mock_client.embeddings.create.assert_called_once()
