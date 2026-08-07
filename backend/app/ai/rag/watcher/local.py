import threading
import time

from .base import BaseWatcher


class LocalWatcher(BaseWatcher):
    """
    Watch local knowledge base
    and trigger incremental update.
    """

    def __init__(
        self,
        incremental_manager,
        interval: int = 30,
    ):
        self.incremental_manager = incremental_manager
        self.interval = interval

        self.running = False
        self.thread = None

    def _run(self):
        while self.running:
            try:
                self.incremental_manager.update()

            except Exception:
                # watcher should not stop
                # because one scan failed
                pass

            time.sleep(self.interval)

    def start(self):
        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._run,
            daemon=True,
        )

        self.thread.start()

    def stop(self):
        self.running = False

        if self.thread:
            self.thread.join(timeout=1)

            self.thread = None
