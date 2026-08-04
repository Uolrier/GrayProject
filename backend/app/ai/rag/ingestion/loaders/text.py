from typing import List

from ..base import BaseDocumentLoader
from ..factory import LoaderFactory
from ..schema import Document


@LoaderFactory.register("text")
class TextLoader(BaseDocumentLoader):
    """
    Plain text document loader.
    """

    def __init__(self, path: str):
        self.path = path

    def load(self) -> List[Document]:
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
