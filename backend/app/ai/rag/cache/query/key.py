import hashlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.app.ai.rag.query.schema import QueryRequest


def create_query_cache_key(request: "QueryRequest") -> str:
    """
    Create a stable cache key for a query request.

    The key includes the query, knowledge base, and top-k value
    so different query configurations do not collide.
    """

    content = f"{request.knowledge_base}:{request.top_k}:{request.query}"

    return hashlib.sha256(content.encode("utf-8")).hexdigest()
