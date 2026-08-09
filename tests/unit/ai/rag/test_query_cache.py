from datetime import datetime

from backend.app.ai.rag.cache.query import (
    QueryCacheFactory,
    QueryCacheItem,
    create_query_cache_key,
)
from backend.app.ai.rag.query.schema import QueryRequest, QueryResponse


def create_response(request: QueryRequest) -> QueryResponse:
    return QueryResponse(
        query=request.query,
        results=[],
        context=None,
        sources=[],
    )


def test_query_cache_factory():
    cache = QueryCacheFactory.create()

    assert cache is not None


def test_query_cache_get_miss():
    cache = QueryCacheFactory.create()

    assert cache.get("missing") is None


def test_query_cache_set_and_get():
    cache = QueryCacheFactory.create()

    request = QueryRequest(query="hello")

    item = QueryCacheItem(
        key="test-key",
        response=create_response(request),
        created_at=datetime.now(),
    )

    cache.set("test-key", item)

    cached = cache.get("test-key")

    assert cached is not None
    assert cached.key == "test-key"
    assert cached.response.query == "hello"


def test_query_cache_delete():
    cache = QueryCacheFactory.create()

    request = QueryRequest(query="hello")

    item = QueryCacheItem(
        key="test-key",
        response=create_response(request),
        created_at=datetime.now(),
    )

    cache.set("test-key", item)
    cache.delete("test-key")

    assert cache.get("test-key") is None


def test_query_cache_clear():
    cache = QueryCacheFactory.create()

    request = QueryRequest(query="hello")

    item = QueryCacheItem(
        key="test-key",
        response=create_response(request),
        created_at=datetime.now(),
    )

    cache.set("test-key", item)
    cache.clear()

    assert cache.get("test-key") is None


def test_query_cache_key_is_stable():
    request1 = QueryRequest(
        query="hello",
        knowledge_base="default",
        top_k=5,
    )

    request2 = QueryRequest(
        query="hello",
        knowledge_base="default",
        top_k=5,
    )

    assert create_query_cache_key(request1) == create_query_cache_key(request2)


def test_query_cache_key_changes_with_knowledge_base():
    request1 = QueryRequest(
        query="hello",
        knowledge_base="default",
        top_k=5,
    )

    request2 = QueryRequest(
        query="hello",
        knowledge_base="other",
        top_k=5,
    )

    assert create_query_cache_key(request1) != create_query_cache_key(request2)


def test_query_cache_key_changes_with_top_k():
    request1 = QueryRequest(
        query="hello",
        knowledge_base="default",
        top_k=5,
    )

    request2 = QueryRequest(
        query="hello",
        knowledge_base="default",
        top_k=10,
    )

    assert create_query_cache_key(request1) != create_query_cache_key(request2)


def test_query_cache_key_changes_with_query():
    request1 = QueryRequest(
        query="hello",
        knowledge_base="default",
        top_k=5,
    )

    request2 = QueryRequest(
        query="world",
        knowledge_base="default",
        top_k=5,
    )

    assert create_query_cache_key(request1) != create_query_cache_key(request2)
