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
