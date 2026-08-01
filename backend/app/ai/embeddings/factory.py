"""Embedding factory."""

from .base import BaseEmbedding
from .registry import get_embedding


class EmbeddingFactory:
    """
    Factory for creating embedding instances.
    """

    @classmethod
    def create(
        cls,
        provider: str,
        **kwargs,
    ) -> BaseEmbedding:
        """
        Create embedding instance.

        Example:
            EmbeddingFactory.create("bge")
        """

        embedding_cls = get_embedding(provider)

        return embedding_cls(**kwargs)
