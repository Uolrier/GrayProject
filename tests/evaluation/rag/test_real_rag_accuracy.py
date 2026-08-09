import json
from pathlib import Path

from backend.app.ai.rag.evaluation.evaluator import (
    RetrievalEvaluator,
)
from backend.app.ai.rag.evaluation.schema import (
    RetrievalEvaluationCase,
)
from backend.app.ai.rag.retrieval.vector_retriever import (
    VectorRetriever,
)
from tests.evaluation.rag.fixtures.build_eval_index import (
    DummyEmbedding,
    build_eval_vector_store,
)

DATASET_PATH = Path("tests/evaluation/rag/datasets/grayproject_eval.json")


def load_cases():
    with open(
        DATASET_PATH,
        "r",
        encoding="utf-8",
    ) as f:
        data = json.load(f)

    return [
        RetrievalEvaluationCase(
            query=item["query"],
            expected_sources=item["expected_sources"],
            expected_keywords=item.get("expected_keywords"),
        )
        for item in data
    ]


def test_real_rag_accuracy():
    vector_store = build_eval_vector_store()

    retriever = VectorRetriever(
        embedding=DummyEmbedding(),
        vector_store=vector_store,
    )

    evaluator = RetrievalEvaluator(
        retriever=retriever,
    )

    cases = load_cases()

    results = evaluator.evaluate(
        cases,
        top_k=5,
    )

    hit_count = sum(1 for result in results if result.hit)

    hit_rate = hit_count / len(results)

    print(
        "\nHit Rate:",
        hit_rate,
    )

    for result in results:
        print(
            result.query,
            "=>",
            result.retrieved_sources,
            "hit=",
            result.hit,
        )

    assert hit_rate >= 0.8
