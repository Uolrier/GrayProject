import time
from pathlib import Path

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


def test_large_rebuild(
    tmp_path,
    monkeypatch,
):
    """
    Large RAG rebuild benchmark.
    """

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

    dataset = Path(__file__).resolve().parents[2] / "assets" / "rag_large_dataset"

    assert dataset.exists()

    config = KnowledgeBaseConfig(
        name="rebuild_test_kb",
        type="local",
        embedding="dummy",
        vectordb="chroma",
        root_path=str(dataset),
    )

    manager = KnowledgeBaseManager(
        persistence=KnowledgeBasePersistence(tmp_path / "knowledge_bases.json")
    )

    kb = manager.create(config)

    # initial index

    kb.add(str(dataset))

    before = kb.vector_store.count()

    start = time.perf_counter()

    result = kb.rebuild()

    elapsed = time.perf_counter() - start

    after = kb.vector_store.count()

    print()
    print("==============================")
    print("Large RAG Rebuild Benchmark")
    print("==============================")
    print(f"Initial vectors: {before}")
    print(f"Rebuild result: {result}")
    print(f"Rebuilt vectors: {after}")
    print(f"Time: {elapsed:.2f}s")
    print("==============================")

    assert before > 0

    assert after == before
