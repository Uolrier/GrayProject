from pathlib import Path

from ..base import BaseDocumentLoader
from ..schema import Document


class JavaScriptLoader(BaseDocumentLoader):
    """
    Loader for JavaScript / TypeScript source files.

    Supported:
    - .js
    - .jsx
    - .ts
    - .tsx
    """

    extensions = {
        ".js",
        ".jsx",
        ".ts",
        ".tsx",
    }

    def load(self, path: str) -> Document:
        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError(path)

        content = file_path.read_text(encoding="utf-8")

        return Document(
            page_content=content,
            metadata={
                "source": str(file_path),
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
