from unittest.mock import MagicMock

from app.ai.rag.watcher.local import LocalWatcher
from app.ai.rag.watcher.manager import WatcherManager


def test_local_watcher():
    manager = MagicMock()

    watcher = LocalWatcher(
        incremental_manager=manager,
        interval=1,
    )

    watcher.start()

    assert watcher.running

    watcher.stop()

    assert not watcher.running


def test_watcher_manager():
    manager = MagicMock()

    watcher_manager = WatcherManager()

    watcher_manager.create_local(
        "local",
        manager,
    )

    assert "local" in watcher_manager.watchers
