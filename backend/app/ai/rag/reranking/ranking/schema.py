from dataclasses import dataclass, field


@dataclass
class RankedDocument:
    """
    Document used during ranking pipeline.
    """

    id: str
    content: str

    retrieval_score: float = 0.0
    rerank_score: float = 0.0
    final_score: float = 0.0

    metadata: dict = field(default_factory=dict)
