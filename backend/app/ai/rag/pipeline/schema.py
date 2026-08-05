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


@dataclass
class EmbeddedChunk:
    """
    Document chunk with vector embedding.

    Attributes:
        id: Unique chunk id.
        document_id: Source document id.
        text: Original chunk text.
        embedding: Vector representation.
        metadata: Additional information.
    """

    id: str

    document_id: str

    text: str

    embedding: list[float]

    metadata: Dict[str, Any] = field(default_factory=dict)
