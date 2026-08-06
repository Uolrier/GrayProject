from dataclasses import dataclass
from typing import Any


@dataclass
class RerankDocument:
    id: str
    text: str
    metadata: dict[str, Any] | None = None


@dataclass
class RerankItem:
    id: str
    score: float
    text: str
    metadata: dict[str, Any] | None = None


@dataclass
class RerankRequest:
    query: str
    documents: list[RerankDocument]
    top_k: int = 5


@dataclass
class RerankResult:
    items: list[RerankItem]
