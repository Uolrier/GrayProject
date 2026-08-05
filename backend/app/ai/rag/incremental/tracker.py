import json
from pathlib import Path

from .schema import (
    ChangeType,
    FileChange,
    FileState,
)


class FileTracker:
    """
    Track document changes between snapshots.
    """

    def __init__(
        self,
        storage_path: str,
    ):
        self.storage_path = Path(storage_path)

    def load(self) -> dict[str, FileState]:
        """
        Load previous snapshot.
        """

        if not self.storage_path.exists():
            return {}

        with self.storage_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        return {path: FileState(**state) for path, state in data.items()}

    def save(
        self,
        snapshot: dict[str, FileState],
    ):
        """
        Save current snapshot.
        """

        self.storage_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        data = {
            path: {
                "path": state.path,
                "hash": state.hash,
                "size": state.size,
                "modified_time": state.modified_time,
            }
            for path, state in snapshot.items()
        }

        with self.storage_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=2,
            )

    def detect_changes(
        self,
        current: dict[str, FileState],
    ) -> list[FileChange]:
        """
        Compare snapshots.
        """

        previous = self.load()

        changes = []

        previous_paths = set(previous.keys())

        current_paths = set(current.keys())

        # new files
        for path in current_paths - previous_paths:
            changes.append(
                FileChange(
                    path=path,
                    change_type=ChangeType.NEW,
                    current=current[path],
                )
            )

        # deleted files
        for path in previous_paths - current_paths:
            changes.append(
                FileChange(
                    path=path,
                    change_type=ChangeType.DELETED,
                    previous=previous[path],
                )
            )

        # updated files
        for path in previous_paths & current_paths:
            old = previous[path]

            new = current[path]

            if old.hash != new.hash:
                changes.append(
                    FileChange(
                        path=path,
                        change_type=ChangeType.UPDATED,
                        previous=old,
                        current=new,
                    )
                )

        return changes
