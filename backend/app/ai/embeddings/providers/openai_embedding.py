"""
OpenAI Embedding provider.
"""

from openai import OpenAI

from config.settings import settings

from ..base import BaseEmbedding
from ..registry import register_embedding


@register_embedding("openai")
class OpenAIEmbedding(BaseEmbedding):
    """
    OpenAI embedding implementation.
    """

    def __init__(
        self,
        model: str | None = None,
    ):
        self.model = model or settings.OPENAI_EMBEDDING_MODEL

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
            base_url=settings.OPENAI_BASE_URL,
        )

    @property
    def model_name(self) -> str:
        """
        Current embedding model name.
        """
        return self.model

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        """
        Single text embedding.
        """

        response = self.client.embeddings.create(
            model=self.model,
            input=text,
        )

        return response.data[0].embedding

    def embed_query(
        self,
        text: str,
    ) -> list[float]:
        """
        Query embedding.

        Alias of embed_text.
        """

        return self.embed_text(text)

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        Batch document embeddings.
        """

        response = self.client.embeddings.create(
            model=self.model,
            input=texts,
        )

        return [item.embedding for item in response.data]
