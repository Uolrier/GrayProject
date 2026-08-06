from backend.app.ai.rag.vectorstore.chroma import ChromaVectorStore
from backend.app.ai.rag.vectorstore.schema import VectorRecord


def test_chroma_metadata_filter(tmp_path):
    store = ChromaVectorStore(persist_dir=str(tmp_path))

    records = [
        VectorRecord(
            id="python",
            text="python code",
            embedding=[0.1, 0.2, 0.3],
            metadata={"language": "python"},
        ),
        VectorRecord(
            id="java",
            text="java code",
            embedding=[0.1, 0.2, 0.3],
            metadata={"language": "java"},
        ),
    ]

    store.add(records)

    results = store.query(
        embedding=[0.1, 0.2, 0.3],
        filters={"language": "python"},
    )

    assert len(results) == 1

    assert results[0].id == "python"

    assert results[0].metadata["language"] == "python"
