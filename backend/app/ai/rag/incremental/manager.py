from typing import Callable

from .scanner import FileScanner
from .schema import (
    ChangeType,
    FileChange,
)
from .tracker import FileTracker


class IncrementalManager:
    """
    Manage incremental document updates.
    """

    def __init__(
        self,
        scanner: FileScanner,
        tracker: FileTracker,
        document_loader: Callable | None = None,
        pipeline=None,
    ):
        self.scanner = scanner

        self.tracker = tracker

        self.document_loader = document_loader

        self.pipeline = pipeline

    def update(
        self,
    ) -> list[FileChange]:
        """
        Detect and process changes.
        """

        current_snapshot = self.scanner.scan()

        changes = self.tracker.detect_changes(current_snapshot)

        if self.pipeline and self.document_loader:
            self._apply_changes(changes)

        self.tracker.save(current_snapshot)

        return changes

    def _apply_changes(
        self,
        changes: list[FileChange],
    ):
        """
        Apply changes to index pipeline.
        """

        for change in changes:
            if change.change_type == ChangeType.NEW:
                documents = self.document_loader(self._resolve_path(change.path))

                for document in documents:
                    self.pipeline.add_document(document)

            elif change.change_type == ChangeType.UPDATED:
                documents = self.document_loader(self._resolve_path(change.path))

                for document in documents:
                    self.pipeline.update_document(document)

            elif change.change_type == ChangeType.DELETED:
                self.pipeline.delete_document(self._resolve_path(change.path))

    def _resolve_path(
        self,
        path: str,
    ) -> str:
        """
        Resolve relative document path.
        """

        from pathlib import Path

        return str(Path(self.scanner.root_path) / path)
