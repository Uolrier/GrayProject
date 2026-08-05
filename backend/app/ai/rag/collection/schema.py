from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class CollectionInfo:
    """
    Collection metadata.
    """

    name: str

    description: str | None = None

    document_count: int = 0

    created_at: datetime = field(default_factory=datetime.utcnow)

    metadata: dict[str, Any] = field(default_factory=dict)
