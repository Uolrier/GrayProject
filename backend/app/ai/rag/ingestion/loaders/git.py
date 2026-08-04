import subprocess
import tempfile
from pathlib import Path

from ..base import BaseDocumentLoader
from ..factory import LoaderFactory
from ..schema import Document


@LoaderFactory.register("git")
class GitLoader(BaseDocumentLoader):
    """
    Loader for Git repositories.

    It scans repository files and delegates
    parsing to existing document loaders.
    """

    IGNORE_DIRS = {
        ".git",
        "node_modules",
        "__pycache__",
        "dist",
        "build",
        ".venv",
        "venv",
    }

    EXTENSION_MAP = {
        ".py": "python",
        ".cpp": "cpp",
        ".cc": "cpp",
        ".h": "cpp",
        ".java": "java",
        ".js": "javascript",
        ".ts": "javascript",
        ".md": "markdown",
        ".json": "json",
        ".txt": "text",
        ".html": "html",
    }

    def load(self, path: str) -> list[Document]:
        repo_path = self._prepare_repo(path)

        documents = []

        for file_path in repo_path.rglob("*"):
            if not file_path.is_file():
                continue

            if self._ignored(file_path):
                continue

            loader_name = self.EXTENSION_MAP.get(file_path.suffix.lower())

            if not loader_name:
                continue

            try:
                loader = LoaderFactory.create(
                    loader_name,
                    path=str(file_path),
                )

                documents.extend(loader.load())

            except TypeError:
                loader = LoaderFactory.create(
                    loader_name,
                )

                documents.extend(loader.load(str(file_path)))

        return documents

    def _prepare_repo(self, source: str) -> Path:
        path = Path(source)

        if path.exists():
            return path

        temp_dir = Path(tempfile.mkdtemp())

        subprocess.run(
            [
                "git",
                "clone",
                source,
                str(temp_dir),
            ],
            check=True,
        )

        return temp_dir

    def _ignored(self, path: Path) -> bool:
        return any(part in self.IGNORE_DIRS for part in path.parts)
