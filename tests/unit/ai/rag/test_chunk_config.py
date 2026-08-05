from backend.app.ai.rag.config import ChunkConfig
from backend.app.ai.rag.pipeline.chunker import (
    FixedLengthChunker,
    OverlapChunker,
)


def test_chunk_config_default():
    config = ChunkConfig()

    assert config.fixed_chunk_size == 500
    assert config.overlap == 50


def test_fixed_chunker_config():
    config = ChunkConfig(fixed_chunk_size=100)

    chunker = FixedLengthChunker(config=config)

    assert chunker.chunk_size == 100


def test_overlap_chunker_config():
    config = ChunkConfig(
        overlap_chunk_size=200,
        overlap=20,
    )

    chunker = OverlapChunker(config=config)

    assert chunker.chunk_size == 200
    assert chunker.overlap == 20
