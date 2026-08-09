from pathlib import Path

from ..base import BaseDocumentLoader
from ..factory import LoaderFactory
from ..schema import Document


@LoaderFactory.register("java")
class JavaLoader(BaseDocumentLoader):
    def __init__(self, path: str | None = None):
        self.path = Path(path) if path else None

    def load(self, path: str | None = None):
        file_path = Path(path) if path else self.path

        if file_path is None:
            raise ValueError("path required")

        if file_path.suffix.lower() != ".java":
            raise ValueError("JavaLoader only supports .java files")

        content = file_path.read_text(encoding="utf-8")

        return Document(
            page_content=content,
            metadata={
                "source": str(file_path),
                "type": "java",
                "language": "java",
                "extension": file_path.suffix,
            },
        )

    def iter_load(self):
        yield self.load()
