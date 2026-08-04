from pathlib import Path

from ..base import BaseDocumentLoader
from ..schema import Document


class CppLoader(BaseDocumentLoader):
    """
    Loader for C/C++ source files.

    Supported extensions:
    .c .h .cpp .cc .hpp
    """

    extensions = {
        ".c",
        ".h",
        ".cpp",
        ".cc",
        ".hpp",
    }

    def load(self, path: str) -> Document:
        file_path = Path(path)

        content = file_path.read_text(encoding="utf-8")

        return Document(
            page_content=content,
            metadata={
                "source": str(file_path),
                "language": "cpp",
            },
        )
