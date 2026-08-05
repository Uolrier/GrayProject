from backend.app.ai.rag.incremental.schema import (
    ChangeType,
    FileState,
)
from backend.app.ai.rag.incremental.tracker import FileTracker


def test_tracker_detect_changes(tmp_path):
    tracker = FileTracker(str(tmp_path / "snapshot.json"))

    old = {
        "a.txt": FileState(
            path="a.txt",
            hash="old",
            size=3,
            modified_time=1,
        )
    }

    tracker.save(old)

    new = {
        "a.txt": FileState(
            path="a.txt",
            hash="new",
            size=4,
            modified_time=2,
        ),
        "b.txt": FileState(
            path="b.txt",
            hash="xxx",
            size=3,
            modified_time=1,
        ),
    }

    changes = tracker.detect_changes(new)

    types = {item.path: item.change_type for item in changes}

    assert types["a.txt"] == ChangeType.UPDATED

    assert types["b.txt"] == ChangeType.NEW
