from backend.app.ai.rag.vectorstore.chroma import ChromaVectorStore
from backend.app.ai.rag.vectorstore.schema import VectorRecord


def test_chroma_add_query(tmp_path):
    store = ChromaVectorStore(persist_dir=str(tmp_path))

    record = VectorRecord(
        id="1", text="hello rag", embedding=[0.1, 0.2, 0.3], metadata={"source": "test"}
    )

    store.add([record])

    assert store.count() == 1

    result = store.query([0.1, 0.2, 0.3])

    assert result[0].text == "hello rag"
