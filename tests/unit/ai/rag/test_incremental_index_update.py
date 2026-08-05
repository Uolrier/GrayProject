from pathlib import Path

from backend.app.ai.rag.incremental import (
    FileScanner,
    FileTracker,
    IncrementalManager,
)
from backend.app.ai.rag.index_update import (
    IndexUpdateManager,
)
from backend.app.ai.rag.metadata import (
    Metadata,
    MetadataManager,
)


class DummyDocument:
    def __init__(
        self,
        document_id,
        content,
        source,
    ):
        self.id = document_id

        self.content = content

        self.metadata = {
            "source": source,
        }


class DummyPipeline:
    def __init__(self):
        self.actions = []

    def add_document(
        self,
        document,
    ):
        self.actions.append(("add", document.id))

    def update_document(
        self,
        document,
    ):
        self.actions.append(("update", document.id))

    def delete_document(
        self,
        document_id,
    ):
        self.actions.append(("delete", document_id))


def test_incremental_index_update(
    tmp_path: Path,
):
    doc = tmp_path / "test.md"

    doc.write_text(
        "hello",
        encoding="utf-8",
    )

    pipeline = DummyPipeline()

    metadata_manager = MetadataManager()

    index_updater = IndexUpdateManager(
        index_pipeline=pipeline,
        metadata_manager=metadata_manager,
    )

    def loader(path):
        document = DummyDocument(
            document_id="doc1",
            content=Path(path).read_text(),
            source=str(path),
        )

        metadata_manager.add(
            Metadata(
                document_id="doc1",
                source=str(path),
            )
        )

        return [document]

    scanner = FileScanner(
        str(tmp_path),
        exclude=["state.json"],
    )

    tracker = FileTracker(str(tmp_path / "state.json"))

    manager = IncrementalManager(
        scanner,
        tracker,
        document_loader=loader,
        index_updater=index_updater,
        metadata_manager=metadata_manager,
    )

    # NEW

    changes = manager.update()

    assert len(changes) == 1

    assert pipeline.actions == [("add", "doc1")]

    # UPDATE

    doc.write_text(
        "hello world",
        encoding="utf-8",
    )

    changes = manager.update()

    assert len(changes) == 1

    assert pipeline.actions[-1] == (
        "update",
        "doc1",
    )

    # DELETE

    doc.unlink()

    changes = manager.update()

    assert len(changes) == 1

    assert pipeline.actions[-1] == (
        "delete",
        "doc1",
    )
