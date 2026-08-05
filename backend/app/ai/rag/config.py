from dataclasses import dataclass


@dataclass
class ChunkConfig:
    """
    Configuration for RAG chunking.
    """

    fixed_chunk_size: int = 500

    overlap_chunk_size: int = 500
    overlap: int = 50

    code_chunk_size: int = 500

    semantic_similarity_threshold: float = 0.3
    semantic_max_chunk_size: int = 500
