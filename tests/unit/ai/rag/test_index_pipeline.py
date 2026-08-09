import threading
import time

from backend.app.ai.rag.pipeline import (
    DocumentChunk,
    IndexPipeline,
    OverlapChunker,
)


def test_overlap_chunker():
    chunker = OverlapChunker(
        chunk_size=5,
        overlap=1,
    )

    result = chunker.split("hello world")

    assert len(result) > 1


def test_document_chunk():
    chunk = DocumentChunk(
        id="1",
        document_id="doc1",
        text="hello",
    )

    assert chunk.text == "hello"


def test_index_pipeline_without_dependencies():
    pipeline = IndexPipeline()

    result = pipeline.run([])

    assert result["documents"] == 0


def test_index_pipeline_streaming():
    from backend.app.ai.rag.ingestion.schema import Document

    documents = [
        Document(
            page_content="hello world",
            metadata={"source": "test.txt"},
        ),
        Document(
            page_content="gray project",
            metadata={"source": "test.txt"},
        ),
    ]

    pipeline = IndexPipeline()

    result = pipeline.run_stream(documents)

    assert result["documents"] == 2
    assert result["chunks"] == 2


def test_index_pipeline_streaming_uses_embedding_cache():
    from backend.app.ai.rag.cache import EmbeddingCacheFactory
    from backend.app.ai.rag.ingestion.schema import Document

    class FakeEmbedding:
        def __init__(self):
            self.calls = 0

        @property
        def model_name(self):
            return "fake-model"

        def embed_documents(self, texts):
            self.calls += 1
            return [[0.1, 0.2, 0.3] for _ in texts]

    embedding = FakeEmbedding()
    cache = EmbeddingCacheFactory.create()

    pipeline = IndexPipeline(
        embedding=embedding,
        embedding_cache=cache,
        embedding_batch_size=2,
    )

    documents = [
        Document(
            page_content="hello world",
            metadata={"source": "test.txt"},
        ),
        Document(
            page_content="gray project",
            metadata={"source": "test.txt"},
        ),
    ]

    first = pipeline.run_stream(documents)

    assert first["documents"] == 2
    assert first["chunks"] == 2
    assert embedding.calls == 1

    second = pipeline.run_stream(documents)

    assert second["documents"] == 2
    assert second["chunks"] == 2
    assert embedding.calls == 1


def test_directory_to_index_pipeline_streaming(tmp_path):
    from backend.app.ai.rag.ingestion.directory import (
        DirectoryImporter,
    )

    file = tmp_path / "document.txt"

    file.write_text(
        "hello grayproject",
        encoding="utf-8",
    )

    class FakeEmbedding:
        @property
        def model_name(self):
            return "fake-model"

        def embed_documents(self, texts):
            return [[0.1, 0.2, 0.3] for _ in texts]

    pipeline = IndexPipeline(
        embedding=FakeEmbedding(),
        embedding_batch_size=2,
    )

    importer = DirectoryImporter()

    result = importer.import_directory_stream(
        tmp_path,
        pipeline,
    )

    assert result["documents"] == 1
    assert result["chunks"] == 1


def test_index_pipeline_parallel_respects_worker_count():
    from backend.app.ai.rag.ingestion.schema import Document

    lock = threading.Lock()

    active_workers = 0
    max_active_workers = 0

    class FakeEmbedding:
        @property
        def model_name(self):
            return "fake-model"

        def embed_documents(self, texts):
            nonlocal active_workers
            nonlocal max_active_workers

            with lock:
                active_workers += 1
                max_active_workers = max(
                    max_active_workers,
                    active_workers,
                )

            time.sleep(0.05)

            with lock:
                active_workers -= 1

            return [[0.1, 0.2, 0.3] for _ in texts]

    documents = [
        Document(
            page_content=f"document {index}",
            metadata={"source": f"test-{index}.txt"},
        )
        for index in range(8)
    ]

    pipeline = IndexPipeline(
        embedding=FakeEmbedding(),
        embedding_batch_size=1,
        parallel_workers=2,
    )

    result = pipeline.run_parallel(documents)

    assert result["documents"] == 8
    assert result["chunks"] == 8
    assert max_active_workers >= 2


def test_index_pipeline_parallel_single_worker():
    from backend.app.ai.rag.ingestion.schema import Document

    class FakeEmbedding:
        @property
        def model_name(self):
            return "fake-model"

        def embed_documents(self, texts):
            return [[0.1, 0.2, 0.3] for _ in texts]

    documents = [
        Document(
            page_content=f"document {index}",
            metadata={"source": f"test-{index}.txt"},
        )
        for index in range(4)
    ]

    pipeline = IndexPipeline(
        embedding=FakeEmbedding(),
        embedding_batch_size=1,
        parallel_workers=4,
    )

    result = pipeline.run_parallel(
        documents,
        max_workers=1,
    )

    assert result["documents"] == 4
    assert result["chunks"] == 4


def test_index_pipeline_parallel_invalid_workers():
    from backend.app.ai.rag.ingestion.schema import Document

    class FakeEmbedding:
        @property
        def model_name(self):
            return "fake-model"

        def embed_documents(self, texts):
            return [[0.1, 0.2, 0.3] for _ in texts]

    pipeline = IndexPipeline(
        embedding=FakeEmbedding(),
    )

    documents = [
        Document(
            page_content="hello",
            metadata={"source": "test.txt"},
        ),
    ]

    try:
        pipeline.run_parallel(
            documents,
            max_workers=0,
        )
        assert False
    except ValueError as exc:
        assert "max_workers" in str(exc)


def test_index_pipeline_parallel_preserves_vector_store_write_order():
    from backend.app.ai.rag.ingestion.schema import Document

    class FakeEmbedding:
        @property
        def model_name(self):
            return "fake-model"

        def embed_documents(self, texts):
            return [[float(len(texts)), 0.2, 0.3] for _ in texts]

    class FakeVectorStore:
        def __init__(self):
            self.writes = []

        def add(self, chunks):
            self.writes.append([chunk.text for chunk in chunks])

    documents = [
        Document(
            page_content=f"document {index}",
            metadata={"source": f"test-{index}.txt"},
        )
        for index in range(4)
    ]

    store = FakeVectorStore()

    pipeline = IndexPipeline(
        embedding=FakeEmbedding(),
        vector_store=store,
        embedding_batch_size=1,
        parallel_workers=4,
    )

    result = pipeline.run_parallel(documents)

    assert result["documents"] == 4
    assert result["chunks"] == 4

    assert store.writes == [
        ["document 0"],
        ["document 1"],
        ["document 2"],
        ["document 3"],
    ]


def test_index_pipeline_parallel():
    from backend.app.ai.rag.ingestion.schema import Document

    class FakeEmbedding:
        def __init__(self):
            self.calls = 0

        @property
        def model_name(self):
            return "fake-model"

        def embed_documents(self, texts):
            self.calls += 1
            return [[0.1, 0.2, 0.3] for _ in texts]

    embedding = FakeEmbedding()

    pipeline = IndexPipeline(
        embedding=embedding,
        embedding_batch_size=1,
        parallel_workers=2,
    )

    documents = [
        Document(
            page_content="document one",
            metadata={"source": "one.txt"},
        ),
        Document(
            page_content="document two",
            metadata={"source": "two.txt"},
        ),
        Document(
            page_content="document three",
            metadata={"source": "three.txt"},
        ),
        Document(
            page_content="document four",
            metadata={"source": "four.txt"},
        ),
    ]

    result = pipeline.run_parallel(documents)

    assert result["documents"] == 4
    assert result["chunks"] == 4
    assert embedding.calls == 4


def test_index_pipeline_parallel_uses_embedding_cache():
    from backend.app.ai.rag.cache import EmbeddingCacheFactory
    from backend.app.ai.rag.ingestion.schema import Document

    class FakeEmbedding:
        def __init__(self):
            self.calls = 0

        @property
        def model_name(self):
            return "fake-model"

        def embed_documents(self, texts):
            self.calls += 1
            return [[0.1, 0.2, 0.3] for _ in texts]

    embedding = FakeEmbedding()
    cache = EmbeddingCacheFactory.create()

    pipeline = IndexPipeline(
        embedding=embedding,
        embedding_cache=cache,
        embedding_batch_size=1,
        parallel_workers=2,
    )

    documents = [
        Document(
            page_content="hello world",
            metadata={"source": "test.txt"},
        ),
        Document(
            page_content="gray project",
            metadata={"source": "test.txt"},
        ),
    ]

    first = pipeline.run_parallel(documents)

    assert first["documents"] == 2
    assert first["chunks"] == 2
    assert embedding.calls == 2

    second = pipeline.run_parallel(documents)

    assert second["documents"] == 2
    assert second["chunks"] == 2
    assert embedding.calls == 2


def test_index_pipeline_parallel_without_documents():
    pipeline = IndexPipeline(
        parallel_workers=2,
    )

    result = pipeline.run_parallel([])

    assert result["documents"] == 0
    assert result["chunks"] == 0


def test_index_pipeline_parallel_without_embedding():
    from backend.app.ai.rag.ingestion.schema import Document

    pipeline = IndexPipeline(
        parallel_workers=2,
    )

    documents = [
        Document(
            page_content="hello",
            metadata={"source": "test.txt"},
        ),
    ]

    result = pipeline.run_parallel(documents)

    assert result["documents"] == 0
    assert result["chunks"] == 0
