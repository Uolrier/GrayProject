"""Prompt debug logger."""

from datetime import datetime
from typing import Any


class PromptDebugLogger:
    """
    Store prompt debug records in memory.

    This utility is used during development
    to inspect LLM input messages.
    """

    def __init__(self):
        self.records: list[dict[str, Any]] = []

    def log(
        self,
        messages: list[dict[str, Any]],
        model: str | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Store one prompt debug record.
        """

        record = {
            "timestamp": datetime.now().isoformat(),
            "messages": messages,
            "model": model,
            "params": params or {},
        }

        self.records.append(record)

        return record

    def latest(self) -> dict[str, Any] | None:
        """
        Return latest debug record.
        """

        if not self.records:
            return None

        return self.records[-1]

    def clear(self) -> None:
        """
        Remove all stored records.
        """

        self.records.clear()
