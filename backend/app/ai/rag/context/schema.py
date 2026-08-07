from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class ContextChunk:
    """
    Chunk used for context assembly.
    """

    content: str
    metadata: Dict[str, Any]


@dataclass
class BuiltContext:
    """
    Final assembled context.
    """

    text: str
    chunks: List[ContextChunk]
    token_count: int = 0
