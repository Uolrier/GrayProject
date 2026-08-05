from app.ai.rag.incremental.tracker import FileTracker
from app.ai.rag.metadata.manager import MetadataManager
from app.ai.rag.metadata.schema import Metadata
from app.ai.rag.rebuild import (
    RebuildManager,
    RebuildRequest,
)


def test_rebuild_request():
    request = RebuildRequest(
        collection="test",
        source_path="docs",
    )

    assert request.collection == "test"
    assert request.drop_collection is False


def test_metadata_clear_collection():
    manager = MetadataManager()

    manager.add(
        Metadata(
            document_id="doc1",
            collection="test",
        )
    )

    manager.add(
        Metadata(
            document_id="doc2",
            collection="other",
        )
    )

    removed = manager.clear_collection("test")

    assert removed == ["doc1"]

    assert manager.get("doc1") is None

    assert manager.get("doc2") is not None


def test_tracker_reset(tmp_path):
    snapshot = tmp_path / "snapshot.json"

    tracker = FileTracker(str(snapshot))

    snapshot.write_text(
        "{}",
        encoding="utf-8",
    )

    tracker.reset()

    assert not snapshot.exists()


def test_rebuild_manager():
    called = {"value": False}

    class DummyPipeline:
        def run(self, documents):
            called["value"] = True

            return {"documents": len(documents)}

    manager = RebuildManager(pipeline=DummyPipeline())

    result = manager.rebuild(
        RebuildRequest(
            collection="test",
            source_path="docs",
        )
    )

    assert called["value"]

    assert result["documents"] == 0
