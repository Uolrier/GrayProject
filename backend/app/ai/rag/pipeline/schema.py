from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class DocumentChunk:
    """
    A piece of document generated during indexing.
    """

    id: str

    document_id: str

    text: str

    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Chunk:
    """
    A chunk generated from a document.

    Attributes:
        content: Chunk text content.
        metadata: Additional information about this chunk.
    """

    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)
