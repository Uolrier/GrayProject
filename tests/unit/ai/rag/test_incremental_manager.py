from pathlib import Path

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
