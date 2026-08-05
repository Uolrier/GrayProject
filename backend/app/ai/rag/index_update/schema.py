from dataclasses import dataclass
from enum import Enum


class IndexAction(str, Enum):
    """
    Index update operation type.
    """

    ADD = "add"

    UPDATE = "update"

    DELETE = "delete"


@dataclass
class IndexUpdateTask:
    """
    Index update task description.
    """

    action: IndexAction

    document_id: str

    collection: str

    path: str | None = None
