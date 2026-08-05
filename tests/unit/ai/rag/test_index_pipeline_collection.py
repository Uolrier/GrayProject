from app.ai.rag.pipeline.index_pipeline import (
    IndexPipeline,
)


class DummyStore:
    def __init__(self):
        self.collections = []

    def create_collection(self, name):
        self.collections.append(name)


def test_index_pipeline_collection():
    store = DummyStore()

    IndexPipeline(
        vector_store=store,
        collection_name="python_docs",
    )

    assert "python_docs" in store.collections
