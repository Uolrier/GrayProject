from pathlib import Path
from typing import Iterator, List

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

    def __init__(
        self,
        path: str,
        chunk_size: int = 1024 * 1024,
    ):
        self.path = Path(path)
        self.chunk_size = chunk_size

    def load(self) -> List[Document]:
        """
        Load markdown file.
        """

        if not self.path.exists():
            raise FileNotFoundError(self.path)

        content = self.path.read_text(
            encoding="utf-8",
        )

        return [
            Document(
                page_content=content,
                metadata={
                    "source": str(self.path),
                    "type": ("readme" if is_readme(self.path.name) else "markdown"),
                },
            )
        ]

    def iter_load(self) -> Iterator[Document]:
        """
        Stream markdown file in chunks.
        """

        if not self.path.exists():
            raise FileNotFoundError(self.path)

        document_type = "readme" if is_readme(self.path.name) else "markdown"

        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:
            while True:
                content = file.read(self.chunk_size)

                if not content:
                    break

                yield Document(
                    page_content=content,
                    metadata={
                        "source": str(self.path),
                        "type": document_type,
                    },
                )
