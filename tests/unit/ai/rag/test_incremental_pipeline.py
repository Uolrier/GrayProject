from pathlib import Path

from backend.app.ai.rag.incremental import (
    DocumentLoaderAdapter,
    FileScanner,
    FileTracker,
    IncrementalManager,
)


class DummyPipeline:
    def __init__(self):
        self.added = []

    def add_document(self, document):
        self.added.append(document)

    def update_document(self, document):
        self.added.append(document)

    def delete_document(self, document_id):
        pass


def test_incremental_pipeline_integration(
    tmp_path: Path,
):
    doc = tmp_path / "test.md"

    doc.write_text(
        "# hello",
        encoding="utf-8",
    )

    scanner = FileScanner(
        str(tmp_path),
        exclude=["state.json"],
    )

    tracker = FileTracker(str(tmp_path / "state.json"))

    pipeline = DummyPipeline()

    loader = DocumentLoaderAdapter()

    manager = IncrementalManager(
        scanner,
        tracker,
        document_loader=loader.load,
        pipeline=pipeline,
    )

    changes = manager.update()

    assert len(changes) == 1

    assert len(pipeline.added) == 1

    assert pipeline.added[0].page_content == "# hello"
