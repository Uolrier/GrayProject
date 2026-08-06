from backend.app.ai.rag.index_update import (
    IndexAction,
    IndexUpdateManager,
    IndexUpdateTask,
)


class DummyPipeline:
    def __init__(self):
        self.called = False
        self.documents = None

    def run(self, documents):
        self.called = True
        self.documents = documents
        return "indexed"


class DummyLoaderAdapter:
    def load(self, path):
        return [
            {
                "path": path,
            }
        ]


class DummyVectorStore:
    def __init__(self):
        self.deleted = []

    def delete(self, ids):
        self.deleted.extend(ids)


class DummyMetadata:
    def __init__(self):
        self.deleted = []

    def delete(self, doc_id):
        self.deleted.append(doc_id)


def test_add_index():
    pipeline = DummyPipeline()

    manager = IndexUpdateManager(
        index_pipeline=pipeline,
        loader_adapter=DummyLoaderAdapter(),
    )

    task = IndexUpdateTask(
        action=IndexAction.ADD,
        document_id="doc1",
        collection="default",
        path="test.md",
    )

    result = manager.execute(task)

    assert result == "indexed"
    assert pipeline.called


def test_update_index():
    pipeline = DummyPipeline()

    store = DummyVectorStore()

    manager = IndexUpdateManager(
        index_pipeline=pipeline,
        vector_store=store,
        loader_adapter=DummyLoaderAdapter(),
    )

    task = IndexUpdateTask(
        action=IndexAction.UPDATE,
        document_id="doc1",
        collection="default",
        path="test.md",
    )

    manager.execute(task)

    assert store.deleted == ["doc1"]
    assert pipeline.called


def test_delete_index():
    store = DummyVectorStore()

    metadata = DummyMetadata()

    manager = IndexUpdateManager(
        vector_store=store,
        metadata_manager=metadata,
    )

    task = IndexUpdateTask(
        action=IndexAction.DELETE,
        document_id="doc1",
        collection="default",
    )

    result = manager.execute(task)

    assert result is True
    assert store.deleted == ["doc1"]
    assert metadata.deleted == ["doc1"]
