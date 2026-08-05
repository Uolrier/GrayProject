from backend.app.ai.rag.cache import (
    EmbeddingCacheFactory,
)
from backend.app.ai.rag.pipeline.embedding_pipeline import (
    EmbeddingPipeline,
)
from backend.app.ai.rag.pipeline.schema import (
    DocumentChunk,
)


class FakeEmbedding:
    """
    Fake embedding provider for testing.
    """

    def embed_documents(self, texts):
        return [[0.1, 0.2, 0.3] for _ in texts]


def test_embedding_pipeline():
    chunks = [
        DocumentChunk(
            id="doc1_0",
            document_id="doc1",
            text="hello world",
            metadata={"source": "test.md"},
        ),
        DocumentChunk(
            id="doc1_1",
            document_id="doc1",
            text="rag system",
            metadata={"source": "test.md"},
        ),
    ]

    pipeline = EmbeddingPipeline(embedding=FakeEmbedding())

    result = pipeline.run(chunks)

    assert len(result) == 2

    assert result[0].id == "doc1_0"

    assert result[0].document_id == "doc1"

    assert result[0].text == "hello world"

    assert result[0].embedding == [
        0.1,
        0.2,
        0.3,
    ]

    assert result[0].metadata["source"] == "test.md"


class CacheFakeEmbedding:
    """
    Fake embedding provider with call counter.
    """

    def __init__(self):
        self.calls = 0

    @property
    def model_name(self):
        return "fake-model"

    def embed_documents(self, texts):
        self.calls += 1

        return [[0.1, 0.2, 0.3] for _ in texts]


def test_embedding_pipeline_cache_hit():
    chunks = [
        DocumentChunk(
            id="doc1_0",
            document_id="doc1",
            text="hello world",
        )
    ]

    embedding = CacheFakeEmbedding()

    cache = EmbeddingCacheFactory.create()

    pipeline = EmbeddingPipeline(
        embedding=embedding,
        cache=cache,
    )

    first = pipeline.run(chunks)

    assert len(first) == 1

    assert embedding.calls == 1

    second = pipeline.run(chunks)

    assert len(second) == 1

    assert second[0].embedding == [
        0.1,
        0.2,
        0.3,
    ]

    # 第二次应该命中缓存
    assert embedding.calls == 1
