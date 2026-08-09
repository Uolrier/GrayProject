from unittest.mock import Mock

from backend.app.ai.rag.cache import (
    EmbeddingCacheFactory,
    EmbeddingCacheItem,
    create_embedding_cache_key,
)
from backend.app.ai.rag.pipeline.embedding_pipeline import EmbeddingPipeline
from backend.app.ai.rag.pipeline.schema import DocumentChunk


def create_chunk(
    chunk_id: str,
    text: str,
) -> DocumentChunk:
    return DocumentChunk(
        id=chunk_id,
        document_id="doc-1",
        text=text,
        metadata={},
    )


def create_embedding() -> Mock:
    embedding = Mock()
    embedding.model_name = "bge-small"
    return embedding


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


def test_embedding_pipeline_cache_miss():
    embedding = create_embedding()
    embedding.embed_documents.return_value = [
        [0.1, 0.2, 0.3],
    ]

    cache = EmbeddingCacheFactory.create()

    pipeline = EmbeddingPipeline(
        embedding=embedding,
        cache=cache,
    )

    chunks = [
        create_chunk("chunk-1", "hello"),
    ]

    result = pipeline.run(chunks)

    assert len(result) == 1
    assert result[0].embedding == [0.1, 0.2, 0.3]

    embedding.embed_documents.assert_called_once_with(
        ["hello"],
    )

    key = create_embedding_cache_key(
        "hello",
        "bge-small",
    )

    cached = cache.get(key)

    assert cached is not None
    assert cached.vector == [0.1, 0.2, 0.3]


def test_embedding_pipeline_cache_hit():
    embedding = create_embedding()
    embedding.embed_documents.return_value = [
        [0.1, 0.2, 0.3],
    ]

    cache = EmbeddingCacheFactory.create()

    pipeline = EmbeddingPipeline(
        embedding=embedding,
        cache=cache,
    )

    chunks = [
        create_chunk("chunk-1", "hello"),
    ]

    first_result = pipeline.run(chunks)

    assert first_result[0].embedding == [0.1, 0.2, 0.3]

    embedding.embed_documents.reset_mock()

    second_result = pipeline.run(chunks)

    assert second_result[0].embedding == [0.1, 0.2, 0.3]

    embedding.embed_documents.assert_not_called()


def test_embedding_pipeline_partial_cache_hit():
    embedding = create_embedding()
    embedding.embed_documents.side_effect = [
        [
            [0.1, 0.2, 0.3],
            [0.7, 0.8, 0.9],
        ],
    ]

    cache = EmbeddingCacheFactory.create()

    cached_key = create_embedding_cache_key(
        "hello",
        "bge-small",
    )

    cache.set(
        cached_key,
        EmbeddingCacheItem(
            key=cached_key,
            vector=[0.1, 0.2, 0.3],
            model="bge-small",
            created_at=None,
        ),
    )

    pipeline = EmbeddingPipeline(
        embedding=embedding,
        cache=cache,
    )

    chunks = [
        create_chunk("chunk-1", "hello"),
        create_chunk("chunk-2", "world"),
        create_chunk("chunk-3", "test"),
    ]

    result = pipeline.run(chunks)

    assert [chunk.embedding for chunk in result] == [
        [0.1, 0.2, 0.3],
        [0.1, 0.2, 0.3],
        [0.7, 0.8, 0.9],
    ]
    embedding.embed_documents.assert_called_once_with(
        ["world", "test"],
    )


def test_embedding_pipeline_cache_none():
    embedding = create_embedding()
    embedding.embed_documents.return_value = [
        [0.1, 0.2, 0.3],
    ]

    pipeline = EmbeddingPipeline(
        embedding=embedding,
        cache=None,
    )

    chunks = [
        create_chunk("chunk-1", "hello"),
    ]

    result = pipeline.run(chunks)

    assert result[0].embedding == [0.1, 0.2, 0.3]

    embedding.embed_documents.assert_called_once_with(
        ["hello"],
    )
