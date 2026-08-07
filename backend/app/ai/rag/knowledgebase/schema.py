from dataclasses import dataclass, field

from app.ai.rag.retrieval.schema import RetrievedDocument


@dataclass(slots=True)
class KnowledgeBaseConfig:
    """
    Knowledge base configuration.
    """

    name: str

    type: str

    embedding: str

    vectordb: str

    reranker: str | None = None

    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class KnowledgeBaseSearchResult:
    """
    Knowledge base search result.
    """

    query: str

    documents: list[RetrievedDocument]

    metadata: dict[str, str] = field(default_factory=dict)
