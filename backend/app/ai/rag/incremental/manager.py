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
        document_state_manager=None,
    ):
        self.scanner = scanner

        self.tracker = tracker

        self.document_loader = document_loader

        self.metadata_manager = metadata_manager

        self.document_state_manager = document_state_manager
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

        if self.document_state_manager:
            self._update_document_states(changes)

        if self.index_updater and self.document_loader:
            self._apply_changes(changes)

        self.tracker.save(current_snapshot)

        return changes

    def _update_document_states(
        self,
        changes: list[FileChange],
    ):
        from ..document_state.schema import (
            DocumentStatus,
        )

        for change in changes:
            path = change.path

            if change.change_type == ChangeType.NEW:
                self.document_state_manager.register(
                    path,
                    change.current.hash,
                )

            elif change.change_type == ChangeType.UPDATED:
                self.document_state_manager.update_status(
                    path,
                    DocumentStatus.PARSING,
                )

            elif change.change_type == ChangeType.DELETED:
                self.document_state_manager.update_status(
                    path,
                    DocumentStatus.DELETED,
                )

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

                    if self.document_state_manager:
                        from ..document_state.schema import (
                            DocumentStatus,
                        )

                        self.document_state_manager.update_status(
                            change.path,
                            DocumentStatus.INDEXED,
                        )

            elif change.change_type == ChangeType.UPDATED:
                documents = self.document_loader(self._resolve_path(change.path))

                for document in documents:
                    self.index_updater.update(document)

                    if self.document_state_manager:
                        from ..document_state.schema import (
                            DocumentStatus,
                        )

                        self.document_state_manager.update_status(
                            change.path,
                            DocumentStatus.INDEXED,
                        )

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

                    if self.document_state_manager:
                        from ..document_state.schema import (
                            DocumentStatus,
                        )

                        self.document_state_manager.update_status(
                            change.path,
                            DocumentStatus.DELETED,
                        )

    def _resolve_path(
        self,
        path: str,
    ) -> str:
        """
        Resolve relative document path.
        """

        from pathlib import Path

        return str(Path(self.scanner.root_path) / path)
