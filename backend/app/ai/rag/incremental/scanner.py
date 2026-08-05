import hashlib
from pathlib import Path

from .schema import FileState


class FileScanner:
    """
    Scan documents and generate file snapshots.
    """

    def __init__(
        self,
        root_path: str,
        extensions: list[str] | None = None,
        exclude: list[str] | None = None,
    ):
        self.root_path = Path(root_path)

        self.extensions = extensions

        self.exclude = set(exclude or [])

    def scan(self) -> dict[str, FileState]:
        """
        Scan all files.

        Returns:
            {
                path: FileState
            }
        """

        result = {}

        if not self.root_path.exists():
            return result

        for file_path in self.root_path.rglob("*"):
            if not file_path.is_file():
                continue

            if file_path.name in self.exclude:
                continue

            if not self._allow_file(file_path):
                continue

            state = self._build_state(file_path)

            relative_path = str(file_path.relative_to(self.root_path))

            result[relative_path] = state

        return result

    def _allow_file(
        self,
        path: Path,
    ) -> bool:
        """
        Check file extension.
        """

        if not self.extensions:
            return True

        return path.suffix.lower() in self.extensions

    def _build_state(
        self,
        path: Path,
    ) -> FileState:
        """
        Create file snapshot.
        """

        return FileState(
            path=str(path),
            hash=self._calculate_hash(path),
            size=path.stat().st_size,
            modified_time=path.stat().st_mtime,
        )

    def _calculate_hash(
        self,
        path: Path,
    ) -> str:
        """
        Calculate SHA256 hash.
        """

        sha256 = hashlib.sha256()

        with path.open("rb") as file:
            while chunk := file.read(8192):
                sha256.update(chunk)

        return sha256.hexdigest()
