from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class DocumentStatus(str, Enum):
    NEW = "new"

    PARSING = "parsing"

    PARSED = "parsed"

    EMBEDDING = "embedding"

    INDEXED = "indexed"

    FAILED = "failed"

    DELETED = "deleted"


@dataclass
class DocumentState:
    path: str

    hash: str

    status: DocumentStatus

    updated_at: datetime

    error: Optional[str] = None
