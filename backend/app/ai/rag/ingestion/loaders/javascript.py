from pathlib import Path

from ..base import BaseDocumentLoader
from ..factory import LoaderFactory
from ..schema import Document


@LoaderFactory.register("javascript")
class JavaScriptLoader(BaseDocumentLoader):
    extensions = {
        ".js",
        ".jsx",
        ".ts",
        ".tsx",
    }

    def __init__(self, path: str | None = None):
        self.path = Path(path) if path else None

    def load(self, path: str | None = None):
        file_path = Path(path) if path else self.path

        if file_path is None:
            raise ValueError("path required")

        if not file_path.exists():
            raise FileNotFoundError(file_path)

        content = file_path.read_text(encoding="utf-8")

        return Document(
            page_content=content,
            metadata={
                "source": str(self.path),
                "type": "javascript",
                "language": self.detect_language(file_path.suffix),
                "extension": file_path.suffix,
            },
        )

    @staticmethod
    def detect_language(ext: str):
        mapping = {
            ".js": "javascript",
            ".jsx": "javascript-react",
            ".ts": "typescript",
            ".tsx": "typescript-react",
        }

        return mapping.get(
            ext.lower(),
            "javascript",
        )
