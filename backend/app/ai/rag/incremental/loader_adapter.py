from pathlib import Path

from backend.app.ai.rag.ingestion.factory import LoaderFactory


class DocumentLoaderAdapter:
    """
    Adapter between incremental update
    and RAG document loaders.
    """

    def __init__(
        self,
        default_loader: str = "text",
    ):
        self.default_loader = default_loader

    def load(
        self,
        path: str,
    ):
        """
        Load document by file path.
        """

        loader_name = self._detect_loader(path)

        loader = LoaderFactory.create(
            loader_name,
            path=path,
        )

        return loader.load()

    def _detect_loader(
        self,
        path: str,
    ) -> str:
        """
        Detect loader from extension.
        """

        suffix = Path(path).suffix.lower()

        mapping = {
            ".md": "md",
            ".markdown": "markdown",
            ".txt": "text",
            ".py": "python",
            ".java": "java",
            ".cpp": "cpp",
            ".html": "html",
            ".json": "json",
            ".pdf": "pdf",
            ".doc": "word",
            ".docx": "word",
        }

        return mapping.get(
            suffix,
            self.default_loader,
        )
