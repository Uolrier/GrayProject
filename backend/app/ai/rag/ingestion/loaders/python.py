from pathlib import Path

from ..base import BaseDocumentLoader
from ..factory import LoaderFactory
from ..schema import Document


@LoaderFactory.register("python")
class PythonLoader(BaseDocumentLoader):
    """
    Loader for Python source files.
    """

    def load(self, path: str) -> list[Document]:
        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError(path)

        content = file_path.read_text(encoding="utf-8")

        return [
            Document(
                page_content=content,
                metadata={
                    "source": str(file_path),
                    "type": "python",
                    "suffix": file_path.suffix,
                },
            )
        ]
