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
