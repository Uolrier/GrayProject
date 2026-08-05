from backend.app.ai.rag.cache import (
    EmbeddingCacheFactory,
    EmbeddingCacheItem,
    create_embedding_cache_key,
)


def test_embedding_cache_create():
    cache = EmbeddingCacheFactory.create()

    assert cache is not None


def test_embedding_cache_set_get():
    cache = EmbeddingCacheFactory.create()

    item = EmbeddingCacheItem(
        key="test-key",
        vector=[0.1, 0.2, 0.3],
        model="bge-small",
        created_at=None,
    )

    cache.set(
        "test-key",
        item,
    )

    result = cache.get("test-key")

    assert result is not None
    assert result.vector == [
        0.1,
        0.2,
        0.3,
    ]


def test_embedding_cache_clear():
    cache = EmbeddingCacheFactory.create()

    item = EmbeddingCacheItem(
        key="test-key",
        vector=[1.0],
        model="test",
        created_at=None,
    )

    cache.set(
        "test-key",
        item,
    )

    cache.clear()

    assert cache.get("test-key") is None


def test_embedding_cache_key_same_input():
    key1 = create_embedding_cache_key(
        "hello",
        "bge-small",
    )

    key2 = create_embedding_cache_key(
        "hello",
        "bge-small",
    )

    assert key1 == key2


def test_embedding_cache_key_different_model():
    key1 = create_embedding_cache_key(
        "hello",
        "bge-small",
    )

    key2 = create_embedding_cache_key(
        "hello",
        "openai",
    )

    assert key1 != key2
