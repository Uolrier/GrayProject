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
        index_updater=None,
        pipeline=None,
        metadata_manager=None,
    ):
        self.scanner = scanner

        self.tracker = tracker

        self.document_loader = document_loader

        self.metadata_manager = metadata_manager

        # Step32 compatibility
        if index_updater is not None:
            self.index_updater = index_updater

        elif pipeline is not None:
            from ..index_update import IndexUpdateManager

            self.index_updater = IndexUpdateManager(
                index_pipeline=pipeline,
                metadata_manager=metadata_manager,
            )

        else:
            self.index_updater = None

        self.metadata_manager = metadata_manager

    def update(
        self,
    ) -> list[FileChange]:
        """
        Detect and process changes.
        """

        current_snapshot = self.scanner.scan()

        changes = self.tracker.detect_changes(current_snapshot)

        if self.index_updater and self.document_loader:
            self._apply_changes(changes)

        self.tracker.save(current_snapshot)

        return changes

    def _apply_changes(
        self,
        changes: list[FileChange],
    ):
        """
        Apply changes through IndexUpdateManager.
        """

        for change in changes:
            if change.change_type == ChangeType.NEW:
                documents = self.document_loader(self._resolve_path(change.path))

                for document in documents:
                    self.index_updater.add(document)

            elif change.change_type == ChangeType.UPDATED:
                documents = self.document_loader(self._resolve_path(change.path))

                for document in documents:
                    self.index_updater.update(document)

            elif change.change_type == ChangeType.DELETED:
                document_id = change.document_id

                if document_id is None and self.metadata_manager:
                    metadata = self.metadata_manager.find_by_source(
                        self._resolve_path(change.path)
                    )

                    if metadata:
                        document_id = metadata.document_id

                if document_id:
                    self.index_updater.delete(document_id)

    def _resolve_path(
        self,
        path: str,
    ) -> str:
        """
        Resolve relative document path.
        """

        from pathlib import Path

        return str(Path(self.scanner.root_path) / path)
