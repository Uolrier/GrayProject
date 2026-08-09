from backend.app.ai.rag.evaluation.evaluator import (
    RetrievalEvaluator,
)
from backend.app.ai.rag.evaluation.metrics import (
    hit_rate,
    mean_reciprocal_rank,
    precision_at_k,
)
from backend.app.ai.rag.evaluation.schema import (
    RetrievalEvaluationCase,
)
from backend.app.ai.rag.retrieval.schema import (
    RetrievedDocument,
)


class DummyRetriever:
    def __init__(self, documents):
        self.documents = documents

    def search(
        self,
        query,
        top_k=5,
    ):
        return self.documents[:top_k]


def test_retrieval_hit():
    retriever = DummyRetriever(
        [
            RetrievedDocument(
                id="1",
                text="knowledge base",
                score=0.95,
                metadata={"source": "knowledgebase.py"},
            ),
        ]
    )

    evaluator = RetrievalEvaluator(retriever)

    case = RetrievalEvaluationCase(
        query="create knowledge base",
        expected_sources=["knowledgebase.py"],
    )

    result = evaluator.evaluate_case(case)

    assert result.hit is True

    assert result.first_hit_rank == 1


def test_retrieval_miss():
    retriever = DummyRetriever(
        [
            RetrievedDocument(
                id="1",
                text="other",
                score=0.5,
                metadata={"source": "other.py"},
            ),
        ]
    )

    evaluator = RetrievalEvaluator(retriever)

    case = RetrievalEvaluationCase(
        query="knowledge base",
        expected_sources=["knowledgebase.py"],
    )

    result = evaluator.evaluate_case(case)

    assert result.hit is False

    assert result.first_hit_rank is None


def test_hit_rate():
    result = hit_rate(
        [
            True,
            True,
            False,
            True,
        ]
    )

    assert result == 0.75


def test_precision_at_k():
    score = precision_at_k(
        retrieved=[
            "a.py",
            "b.py",
            "c.py",
        ],
        expected=[
            "a.py",
            "c.py",
        ],
        k=3,
    )

    assert score == 2 / 3


def test_mean_reciprocal_rank():
    score = mean_reciprocal_rank(
        [
            1,
            2,
            None,
        ]
    )

    assert score == (1 + 0.5 + 0) / 3
