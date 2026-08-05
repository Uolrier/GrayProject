from dataclasses import dataclass
from typing import Dict, List


@dataclass
class VectorRecord:
    id: str
    text: str
    embedding: List[float]
    metadata: Dict


@dataclass
class SearchResult:
    id: str
    text: str
    score: float
    metadata: Dict
