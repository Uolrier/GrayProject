from typing import Iterator, List

from pypdf import PdfReader

from ..base import BaseDocumentLoader
from ..schema import Document


class PDFLoader(BaseDocumentLoader):
    """
    PDF document loader.

    Converts PDF pages into Document objects lazily.
    """

    def __init__(self, path: str):
        self.path = path

    def load(self) -> List[Document]:
        return list(self.iter_load())

    def iter_load(self) -> Iterator[Document]:
        reader = PdfReader(self.path)

        for index, page in enumerate(reader.pages):
            text = page.extract_text()

            if not text:
                continue

            yield Document(
                page_content=text,
                metadata={
                    "source": self.path,
                    "page": index + 1,
                    "type": "pdf",
                },
            )
