from pathlib import Path

from ..base import BaseDocumentLoader
from ..schema import Document


class JavaLoader(BaseDocumentLoader):
    """
    Loader for Java source files.
    """

    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        if path.suffix.lower() != ".java":
            raise ValueError("JavaLoader only supports .java files")

        content = path.read_text(encoding="utf-8")

        return Document(
            page_content=content,
            metadata={
                "source": str(path),
                "type": "java",
                "language": "java",
            },
        )
