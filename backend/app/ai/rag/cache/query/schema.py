from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.app.ai.rag.query.schema import QueryResponse


@dataclass
class QueryCacheItem:
    """
    Cached query response item.
    """

    key: str
    response: "QueryResponse"
    created_at: datetime
