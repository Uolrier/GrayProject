from ..base import BaseEmbedding
from ..registry import register_embedding


@register_embedding("dummy")
class DummyEmbedding(BaseEmbedding):
    """
    Dummy embedding for pipeline testing.
    """

    def __init__(
        self,
        dimension: int = 1024,
    ):
        self.dimension = dimension

    @property
    def model_name(self) -> str:
        return "dummy"

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        return [0.0] * self.dimension

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        return [[0.0] * self.dimension for _ in texts]
