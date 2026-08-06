from backend.app.ai.rag.pipeline.index_pipeline import (
    IndexPipeline,
)
from backend.app.ai.rag.vectorstore.chroma import (
    ChromaVectorStore,
)


class DummyEmbedding:
    def embed_documents(self, texts):
        return [[0.1, 0.2, 0.3] for _ in texts]


class DummyDocument:
    def __init__(self):
        self.page_content = "GrayProject RAG test document"

        self.metadata = {"source": "test"}


def test_index_pipeline_with_collection():
    store = ChromaVectorStore(persist_dir="data/test_collection_chroma")

    pipeline = IndexPipeline(
        embedding=DummyEmbedding(),
        vector_store=store,
        collection_name="python_docs",
    )

    result = pipeline.run([DummyDocument()])

    assert result["documents"] == 1

    assert result["chunks"] > 0

    collection = store.client.get_collection("python_docs")

    assert collection.count() > 0

    store.delete_collection("python_docs")
