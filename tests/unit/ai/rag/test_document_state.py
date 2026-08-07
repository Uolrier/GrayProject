from pathlib import Path
from unittest.mock import MagicMock

from app.ai.rag.document_state.manager import (
    DocumentStateManager,
)
from app.ai.rag.document_state.schema import (
    DocumentStatus,
)
from app.ai.rag.document_state.storage import (
    DocumentStateStorage,
)
from app.ai.rag.incremental import (
    FileScanner,
    FileTracker,
    IncrementalManager,
)


def test_document_state_register(
    tmp_path: Path,
):
    storage = DocumentStateStorage(tmp_path / "state.json")

    manager = DocumentStateManager(storage)

    manager.register(
        "README.md",
        "abc123",
    )

    state = manager.get("README.md")

    assert state["hash"] == "abc123"

    assert state["status"] == DocumentStatus.NEW.value


def test_document_state_update(
    tmp_path: Path,
):
    storage = DocumentStateStorage(tmp_path / "state.json")

    manager = DocumentStateManager(storage)

    manager.register(
        "README.md",
        "abc123",
    )

    manager.update_status(
        "README.md",
        DocumentStatus.INDEXED,
    )

    state = manager.get("README.md")

    assert state["status"] == DocumentStatus.INDEXED.value


def test_document_state_indexed(
    tmp_path: Path,
):
    doc = tmp_path / "README.md"

    doc.write_text(
        "hello",
        encoding="utf-8",
    )

    scanner = FileScanner(
        str(tmp_path),
        exclude=[
            "tracker.json",
            "state.json",
        ],
    )

    tracker = FileTracker(str(tmp_path / "tracker.json"))

    storage = DocumentStateStorage(tmp_path / "state.json")

    state_manager = DocumentStateManager(storage)

    loader = MagicMock()

    loader.return_value = ["document"]

    index_updater = MagicMock()

    manager = IncrementalManager(
        scanner,
        tracker,
        document_loader=loader,
        index_updater=index_updater,
        document_state_manager=state_manager,
    )

    manager.update()

    index_updater.add.assert_called_once()

    state = state_manager.get("README.md")

    assert state["status"] == (DocumentStatus.INDEXED.value)
