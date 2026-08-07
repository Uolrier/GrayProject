from pathlib import Path
from typing import List

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
        directory = Path(directory)

        if not directory.exists():
            raise FileNotFoundError(directory)

        documents = []

        for file_path in self._scan(directory):
            loader_name = self._get_loader_name(file_path)

            if loader_name is None:
                continue

            loader = LoaderFactory.create(
                loader_name,
                path=str(file_path),
            )

            docs = loader.load()

            documents.extend(docs)

        return documents

    def _scan(
        self,
        directory: Path,
    ):
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
    ):
        return self.EXTENSION_MAPPING.get(path.suffix.lower())

    def supported_extensions(self):
        return list(self.EXTENSION_MAPPING.keys())

    def _should_ignore(
        self,
        path: Path,
    ):
        if path.name.startswith("."):
            return True

        if path.stat().st_size == 0:
            return True

        return False
