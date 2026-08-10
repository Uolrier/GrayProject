import statistics
import time
from pathlib import Path

import pytest

from backend.app.ai.rag.knowledgebase.manager import (
    KnowledgeBaseManager,
)
from backend.app.ai.rag.knowledgebase.persistence import (
    KnowledgeBasePersistence,
)
from backend.app.ai.rag.knowledgebase.schema import (
    KnowledgeBaseConfig,
)
from backend.app.ai.rag.vectorstore.chroma import (
    ChromaVectorStore,
)
from tests.performance.rag.benchmark_config import (
    DEFAULT_TOP_K,
    QUERY_COUNT,
)


@pytest.mark.skipif(
    pytest.__version__ is None,
    reason="benchmark only",
)
def test_large_rag_retrieval(
    tmp_path,
    monkeypatch,
):
    """
    Large scale RAG retrieval benchmark.

    Flow:

    dataset
        |
        v
    index
        |
        v
    query
        |
        v
    retrieval latency
    """

    # ------------------------
    # isolate chroma storage
    # ------------------------

    original_init = ChromaVectorStore.__init__

    def patched_init(
        self,
        persist_dir="data/chroma",
        collection_name="grayproject",
    ):
        original_init(
            self,
            persist_dir=str(tmp_path / "chroma"),
            collection_name=collection_name,
        )

    monkeypatch.setattr(
        ChromaVectorStore,
        "__init__",
        patched_init,
    )

    # ------------------------
    # dataset
    # ------------------------

    dataset = Path(__file__).resolve().parents[2] / "assets" / "rag_large_dataset"

    assert dataset.exists()

    # ------------------------
    # create knowledge base
    # ------------------------

    config = KnowledgeBaseConfig(
        name="retrieval_test_kb",
        type="local",
        embedding="dummy",
        vectordb="chroma",
    )

    persistence = KnowledgeBasePersistence(
        path=tmp_path / "knowledge_bases.json",
    )

    manager = KnowledgeBaseManager(
        persistence=persistence,
    )

    kb = manager.create(
        config,
    )

    # ------------------------
    # build index
    # ------------------------

    result = kb.add(
        str(dataset),
    )

    expected_documents = len([p for p in dataset.rglob("*") if p.is_file()])

    assert result["documents"] == expected_documents

    # ------------------------
    # retrieval benchmark
    # ------------------------

    queries = [
        "GrayProject AI system",
        "FastAPI backend",
        "RAG pipeline",
        "vector database",
    ]

    latency = []

    for i in range(QUERY_COUNT):
        query = queries[i % len(queries)]

        start = time.perf_counter()

        result = kb.search(
            query,
            top_k=DEFAULT_TOP_K,
        )

        elapsed = time.perf_counter() - start

        latency.append(elapsed)

        assert result.documents

    avg = statistics.mean(latency)

    p95 = sorted(latency)[int(len(latency) * 0.95)]

    print("\n")
    print("==============================")
    print("Large RAG Retrieval Benchmark")
    print("==============================")
    print(f"Queries: {QUERY_COUNT}")
    print(f"Average latency: {avg:.6f}s")
    print(f"P95 latency: {p95:.6f}s")
    print("==============================")
