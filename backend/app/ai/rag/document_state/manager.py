from datetime import datetime

from .schema import (
    DocumentStatus,
)


class DocumentStateManager:
    def __init__(
        self,
        storage,
    ):
        self.storage = storage

        self.states = storage.load()

    def register(
        self,
        path: str,
        file_hash: str,
    ):
        self.states[path] = {
            "hash": file_hash,
            "status": DocumentStatus.NEW.value,
            "updated_at": datetime.utcnow().isoformat(),
            "error": None,
        }

        self.storage.save(self.states)

    def update_status(
        self,
        path: str,
        status: DocumentStatus,
        error: str | None = None,
    ):
        if path not in self.states:
            return

        self.states[path]["status"] = status.value

        self.states[path]["updated_at"] = datetime.utcnow().isoformat()

        self.states[path]["error"] = error

        self.storage.save(self.states)

    def get(
        self,
        path: str,
    ):
        return self.states.get(path)

    def all(self):
        return self.states
