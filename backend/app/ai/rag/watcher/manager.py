from .local import LocalWatcher


class WatcherManager:
    """
    Manage knowledge base watchers.
    """

    def __init__(self):
        self.watchers = {}

    def register(
        self,
        name,
        watcher,
    ):
        self.watchers[name] = watcher

    def create_local(
        self,
        name,
        incremental_manager,
        interval=30,
    ):
        """
        Create local filesystem watcher.
        """

        watcher = LocalWatcher(
            incremental_manager=incremental_manager,
            interval=interval,
        )

        self.register(
            name,
            watcher,
        )

        return watcher

    def start_all(self):
        for watcher in self.watchers.values():
            watcher.start()

    def stop_all(self):
        for watcher in self.watchers.values():
            watcher.stop()
