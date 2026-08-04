from backend.app.ai.rag.pipeline.chunker import FixedLengthChunker


def test_fixed_length_chunker_basic():
    text = "a" * 1200

    chunker = FixedLengthChunker(
        chunk_size=500,
        overlap=50,
    )

    chunks = chunker.split(text)

    assert len(chunks) == 3

    assert chunks[0].metadata["start"] == 0
    assert chunks[0].metadata["end"] == 500

    assert chunks[1].metadata["start"] == 450


def test_fixed_length_chunker_overlap():
    text = "0123456789ABCDEFGHIJ"

    chunker = FixedLengthChunker(
        chunk_size=10,
        overlap=2,
    )

    chunks = chunker.split(text)

    assert chunks[0].content == "0123456789"
    assert chunks[1].content == "89ABCDEFGH"
    assert chunks[2].content == "GHIJ"


def test_invalid_chunk_size():
    try:
        FixedLengthChunker(chunk_size=0)
        assert False
    except ValueError:
        assert True
