import time
from pathlib import Path

import pytest

from backend.app.ai.rag.knowledgebase.manager import (
    KnowledgeBaseManager,
)
from backend.app.ai.rag.knowledgebase.schema import (
    KnowledgeBaseConfig,
)
from backend.app.ai.rag.vectorstore.chroma import (
    ChromaVectorStore,
)


@pytest.mark.skipif(
    pytest.__version__ is None,
    reason="benchmark only",
)
def test_large_rag_index(
    tmp_path,
    monkeypatch,
):
    """
    Large scale RAG index benchmark.

    Flow:

    dataset
        |
        v
    knowledge base
        |
        v
    loader
        |
        v
    index pipeline
        |
        v
    chroma
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
        name="large_test_kb",
        type="local",
        embedding="dummy",
        vectordb="chroma",
    )

    manager = KnowledgeBaseManager()

    kb = manager.create(
        config,
    )

    # ------------------------
    # benchmark
    # ------------------------

    start = time.perf_counter()

    result = kb.add(
        str(dataset),
    )

    elapsed = time.perf_counter() - start

    # ------------------------
    # statistics
    # ------------------------

    vector_count = kb.vector_store.count()

    print("\n")
    print("==============================")
    print("Large RAG Index Benchmark")
    print("==============================")
    print(f"Documents: {result['documents']}")
    print(f"Chunks: {result['chunks']}")
    print(f"Vectors: {vector_count}")
    print(f"Time: {elapsed:.2f}s")
    print("==============================")

    # ------------------------
    # verify
    # ------------------------

    expected_documents = len([p for p in dataset.rglob("*") if p.is_file()])

    assert result["documents"] == expected_documents

    assert result["chunks"] > 0

    assert vector_count == result["chunks"]
