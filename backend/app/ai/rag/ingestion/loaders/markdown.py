from pathlib import Path
from typing import List

from ..base import BaseDocumentLoader
from ..factory import LoaderFactory
from ..readme import is_readme
from ..schema import Document


@LoaderFactory.register("markdown")
@LoaderFactory.register("md")
class MarkdownLoader(BaseDocumentLoader):
    """
    Loader for Markdown documents.
    """

    def __init__(self, path: str):
        self.path = Path(path)

    def load(self) -> List[Document]:
        """
        Load markdown file.
        """

        if not self.path.exists():
            raise FileNotFoundError(self.path)

        content = self.path.read_text(encoding="utf-8")

        return [
            Document(
                page_content=content,
                metadata={
                    "source": str(self.path),
                    "type": "readme" if is_readme(self.path.name) else "markdown",
                },
            )
        ]
