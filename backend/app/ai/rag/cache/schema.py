from dataclasses import dataclass
from datetime import datetime


@dataclass
class EmbeddingCacheItem:
    """
    Cached embedding vector item.
    """

    key: str

    vector: list[float]

    model: str

    created_at: datetime
