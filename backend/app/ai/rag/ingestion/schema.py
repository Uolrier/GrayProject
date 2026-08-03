from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Document:
    """
    Unified document representation.

    A document is the basic unit entering RAG pipeline.
    """

    page_content: str

    metadata: Dict[str, Any] = field(default_factory=dict)
