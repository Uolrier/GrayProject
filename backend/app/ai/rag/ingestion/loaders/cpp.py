from pathlib import Path

from ..base import BaseDocumentLoader
from ..factory import LoaderFactory
from ..schema import Document


@LoaderFactory.register("cpp")
class CppLoader(BaseDocumentLoader):
    """
    Loader for C/C++ source files.
    """

    extensions = {
        ".c",
        ".h",
        ".cpp",
        ".cc",
        ".hpp",
    }

    def __init__(self, path: str | None = None):
        self.path = Path(path) if path else None

    def load(self, path: str | None = None):
        file_path = Path(path) if path else self.path

        if file_path is None:
            raise ValueError("path required")
        content = file_path.read_text(encoding="utf-8")

        return Document(
            page_content=content,
            metadata={
                "source": str(self.path),
                "language": "cpp",
            },
        )

    def iter_load(self):
        yield self.load()
