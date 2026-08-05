from dataclasses import dataclass
from enum import Enum


class ChangeType(str, Enum):
    """
    Document change type.
    """

    NEW = "new"

    UPDATED = "updated"

    DELETED = "deleted"


@dataclass
class FileState:
    """
    Snapshot information of a file.
    """

    path: str

    hash: str

    size: int

    modified_time: float


@dataclass
class FileChange:
    """
    Incremental change result.
    """

    path: str

    change_type: ChangeType

    previous: FileState | None = None

    current: FileState | None = None
