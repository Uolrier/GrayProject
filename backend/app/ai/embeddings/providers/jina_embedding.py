"""Jina embedding provider."""

from sentence_transformers import SentenceTransformer

from ..base import BaseEmbedding


class JinaEmbedding(BaseEmbedding):
    """
    Jina 本地 Embedding Provider
    """

    def __init__(
        self,
        model_name: str = "jinaai/jina-embeddings-v3",
        device: str = "cpu",
    ) -> None:
        self._model_name = model_name
        self._device = device

        try:
            self._model = SentenceTransformer(
                model_name,
                device=device,
                trust_remote_code=True,
            )
        except Exception as e:
            raise RuntimeError(f"Failed to load embedding model: {model_name}") from e

    @property
    def model_name(self) -> str:
        return self._model_name

    def embed_text(self, text: str) -> list[float]:
        """
        单文本向量化
        """
        try:
            vector = self._model.encode(
                text,
                normalize_embeddings=True,
            )
            return vector.tolist()
        except Exception as e:
            raise RuntimeError("Failed to embed text.") from e

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        批量文本向量化
        """
        try:
            vectors = self._model.encode(
                texts,
                normalize_embeddings=True,
            )
            return vectors.tolist()
        except Exception as e:
            raise RuntimeError("Failed to embed documents.") from e
