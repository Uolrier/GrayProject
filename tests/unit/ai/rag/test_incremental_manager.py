from pathlib import Path

from backend.app.ai.rag.document_state import (
    DocumentStateManager,
    DocumentStateStorage,
    DocumentStatus,
)
from backend.app.ai.rag.incremental import (
    ChangeType,
    FileScanner,
    FileTracker,
    IncrementalManager,
)


def test_incremental_manager(tmp_path: Path):
    doc = tmp_path / "test.md"

    doc.write_text(
        "hello",
        encoding="utf-8",
    )

    scanner = FileScanner(
        str(tmp_path),
        exclude=["state.json"],
    )

    tracker = FileTracker(str(tmp_path / "state.json"))

    manager = IncrementalManager(
        scanner,
        tracker,
    )

    # first scan
    changes = manager.update()

    assert len(changes) == 1

    assert changes[0].change_type == ChangeType.NEW

    # second scan
    changes = manager.update()

    assert len(changes) == 0

    # modify
    doc.write_text(
        "hello world",
        encoding="utf-8",
    )

    changes = manager.update()

    assert len(changes) == 1

    assert changes[0].change_type == ChangeType.UPDATED


def test_incremental_document_state(tmp_path: Path):
    doc = tmp_path / "test.md"

    doc.write_text(
        "hello",
        encoding="utf-8",
    )

    scanner = FileScanner(
        str(tmp_path),
        exclude=[
            "state.json",
            "document_state.json",
        ],
    )

    tracker = FileTracker(str(tmp_path / "state.json"))

    state_storage = DocumentStateStorage(str(tmp_path / "document_state.json"))

    state_manager = DocumentStateManager(state_storage)

    manager = IncrementalManager(
        scanner,
        tracker,
        document_state_manager=state_manager,
    )

    changes = manager.update()

    assert len(changes) == 1

    state = state_manager.get("test.md")

    assert state["status"] == (DocumentStatus.NEW.value)
