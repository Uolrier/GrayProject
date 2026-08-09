from typing import Iterator, List

from ..base import BaseDocumentLoader
from ..factory import LoaderFactory
from ..schema import Document


@LoaderFactory.register("text")
class TextLoader(BaseDocumentLoader):
    """
    Plain text document loader.
    """

    def __init__(
        self,
        path: str,
        chunk_size: int = 1024 * 1024,
    ):
        self.path = path
        self.chunk_size = chunk_size

    def load(self) -> List[Document]:
        """
        Load the complete text file.

        Kept for backward compatibility.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            content = file.read()

        return [
            Document(
                page_content=content,
                metadata={
                    "source": self.path,
                    "type": "txt",
                },
            )
        ]

    def iter_load(self) -> Iterator[Document]:
        """
        Stream a text file in chunks.

        This avoids loading the complete file into memory.
        """
        with open(
            self.path,
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
                        "source": self.path,
                        "type": "txt",
                    },
                )
