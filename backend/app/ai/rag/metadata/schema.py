from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional


@dataclass
class Metadata:
    """
    RAG Metadata
    """

    document_id: str

    source: Optional[str] = None

    collection: Optional[str] = None

    chunk_id: Optional[str] = None

    file_type: Optional[str] = None

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    extra: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self):
        return {
            "document_id": self.document_id,
            "source": self.source,
            "collection": self.collection,
            "chunk_id": self.chunk_id,
            "file_type": self.file_type,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            **self.extra,
        }
