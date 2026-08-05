from app.ai.rag.vectorstore.chroma import (
    ChromaVectorStore,
)


def test_chroma_collection():
    store = ChromaVectorStore(persist_dir="data/test_chroma")

    collection = store.create_collection("test_collection")

    assert collection.name == "test_collection"

    collections = store.list_collections()

    names = [c.name for c in collections]

    assert "test_collection" in names

    store.delete_collection("test_collection")
