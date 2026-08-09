import json
from pathlib import Path

from backend.app.ai.rag.query.pipeline import (
    QueryPipeline,
)
from backend.app.ai.rag.query.schema import (
    QueryRequest,
)


class DummyRetriever:
    def search(
        self,
        query,
        top_k=5,
    ):
        from backend.app.ai.rag.retrieval.schema import (
            RetrievedDocument,
        )

        if "知识库" in query:
            source = "knowledgebase.py"
        else:
            source = "vector_retriever.py"

        return [
            RetrievedDocument(
                id="1",
                text="test",
                score=0.95,
                metadata={
                    "source": source,
                    "chunk_id": "1",
                },
            )
        ]


def load_cases():
    path = Path("tests/evaluation/rag/datasets/retrieval_eval.json")

    with open(
        path,
        encoding="utf-8",
    ) as f:
        return json.load(f)


def test_query_pipeline_accuracy():
    pipeline = QueryPipeline(
        retriever=DummyRetriever(),
    )

    cases = load_cases()

    hits = 0

    for case in cases:
        response = pipeline.run(QueryRequest(query=case["query"]))

        sources = [item.file_path for item in response.sources]

        matched = any(source in case["expected_sources"] for source in sources)

        if matched:
            hits += 1

    accuracy = hits / len(cases)

    assert accuracy >= 0.5
