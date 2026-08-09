from pathlib import Path
from typing import Iterator, List

from .factory import LoaderFactory
from .schema import Document


class DirectoryImporter:
    """
    Import documents from directory.

    Flow:

        Directory
            |
            v
        Loader selection
            |
            v
        Document Loader
            |
            v
        Documents
    """

    DEFAULT_IGNORE_DIRS = {
        ".git",
        ".github",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__",
        ".pytest_cache",
    }

    EXTENSION_MAPPING = {
        ".txt": "text",
        ".md": "markdown",
        ".markdown": "markdown",
        ".py": "python",
        ".java": "java",
        ".cpp": "cpp",
        ".cc": "cpp",
        ".js": "javascript",
        ".json": "json",
        ".html": "html",
        ".htm": "html",
        ".pdf": "pdf",
        ".docx": "word",
    }

    def import_directory(
        self,
        directory: str | Path,
    ) -> List[Document]:
        """
        Import all documents from a directory.

        Kept for backward compatibility.
        """
        return list(self.iter_import_directory(directory))

    def iter_import_directory(
        self,
        directory: str | Path,
    ) -> Iterator[Document]:
        """
        Stream documents from a directory.

        Documents are yielded one by one instead of being
        accumulated in memory.
        """
        directory = Path(directory)

        if not directory.exists():
            raise FileNotFoundError(directory)

        for file_path in self._scan(directory):
            loader_name = self._get_loader_name(file_path)

            if loader_name is None:
                continue

            loader = LoaderFactory.create(
                loader_name,
                path=str(file_path),
            )

            yield from loader.iter_load()

    def _scan(
        self,
        directory: Path,
    ) -> Iterator[Path]:
        for path in directory.rglob("*"):
            if any(part in self.DEFAULT_IGNORE_DIRS for part in path.parts):
                continue

            if path.is_dir():
                continue

            if self._should_ignore(path):
                continue

            yield path

    def _get_loader_name(
        self,
        path: Path,
    ) -> str | None:
        return self.EXTENSION_MAPPING.get(path.suffix.lower())

    def supported_extensions(self) -> list[str]:
        return list(self.EXTENSION_MAPPING.keys())

    def _should_ignore(
        self,
        path: Path,
    ) -> bool:
        if path.name.startswith("."):
            return True

        if path.stat().st_size == 0:
            return True

        return False

    def import_directory_stream(
        self,
        directory: str | Path,
        pipeline,
    ):
        """
        Stream documents from a directory directly into
        an indexing pipeline.
        """
        return pipeline.run_stream(self.iter_import_directory(directory))
