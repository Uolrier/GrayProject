from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class SourceReference:
    """
    Document citation information.

    Represents the original source location
    of retrieved RAG content.
    """

    file_path: str

    chunk_id: str

    score: float

    page: Optional[int] = None

    line_start: Optional[int] = None

    line_end: Optional[int] = None
