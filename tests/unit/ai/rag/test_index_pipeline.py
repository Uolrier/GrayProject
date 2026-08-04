from backend.app.ai.rag.pipeline import (
    DocumentChunk,
    FixedLengthChunker,
    IndexPipeline,
)


def test_fixed_length_chunker():
    chunker = FixedLengthChunker(
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
