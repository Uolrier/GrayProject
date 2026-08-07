from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from backend.app.ai.rag.source.schema import SourceReference


@dataclass
class QueryRequest:
    query: str

    knowledge_base: str = "default"

    top_k: int = 5


@dataclass
class QueryResult:
    content: str

    score: float

    metadata: Dict[str, Any]


@dataclass
class QueryResponse:
    query: str

    results: List[QueryResult]

    context: Optional[str] = None

    sources: List[SourceReference] | None = None
