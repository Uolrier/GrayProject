from backend.app.ai.rag.pipeline.chunker import (
    FixedLengthChunker,
    OverlapChunker,
)


def test_fixed_length_chunker_basic():
    text = "a" * 1200

    chunker = FixedLengthChunker(
        chunk_size=500,
    )

    chunks = chunker.split(text)

    assert len(chunks) == 3

    assert chunks[0].metadata["start"] == 0
    assert chunks[0].metadata["end"] == 500

    assert chunks[1].metadata["start"] == 500


def test_overlap_chunker_basic():
    text = "0123456789ABCDEFGHIJ"

    chunker = OverlapChunker(
        chunk_size=10,
        overlap=2,
    )

    chunks = chunker.split(text)

    assert chunks[0].content == "0123456789"
    assert chunks[1].content == "89ABCDEFGH"
    assert chunks[2].content == "GHIJ"


def test_overlap_chunker_metadata():
    text = "abcdefghij"

    chunker = OverlapChunker(
        chunk_size=6,
        overlap=2,
    )

    chunks = chunker.split(text)

    assert chunks[0].metadata["start"] == 0
    assert chunks[0].metadata["end"] == 6

    assert chunks[1].metadata["start"] == 4


def test_invalid_chunk_size():
    try:
        FixedLengthChunker(
            chunk_size=0,
        )
        assert False
    except ValueError:
        assert True


def test_invalid_overlap():
    try:
        OverlapChunker(
            chunk_size=10,
            overlap=10,
        )
        assert False
    except ValueError:
        assert True
