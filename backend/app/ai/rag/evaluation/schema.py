from dataclasses import dataclass
from typing import List


@dataclass
class RetrievalEvaluationCase:
    """
    Single retrieval evaluation case.
    """

    query: str

    expected_sources: List[str]

    expected_keywords: List[str] | None = None


@dataclass
class RetrievalEvaluationResult:
    """
    Evaluation result for one query.
    """

    query: str

    retrieved_sources: List[str]

    hit: bool

    first_hit_rank: int | None = None
