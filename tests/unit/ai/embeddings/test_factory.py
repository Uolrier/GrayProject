from unittest.mock import MagicMock, patch

from backend.app.ai.embeddings.factory import EmbeddingFactory
from backend.app.ai.embeddings.providers.bge_embedding import BGEEmbedding


@patch("backend.app.ai.embeddings.providers.bge_embedding.SentenceTransformer")
def test_embedding_factory(mock_sentence_transformer):
    mock_sentence_transformer.return_value = MagicMock()

    embedding = EmbeddingFactory.create("bge")

    assert isinstance(
        embedding,
        BGEEmbedding,
    )

    assert embedding.model_name == "BAAI/bge-small-zh-v1.5"
