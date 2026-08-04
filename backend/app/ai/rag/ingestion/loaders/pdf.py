from typing import List

from pypdf import PdfReader

from ..base import BaseDocumentLoader
from ..schema import Document


class PDFLoader(BaseDocumentLoader):
    """
    PDF document loader.

    Converts PDF pages into Document objects.
    """

    def __init__(self, path: str):
        self.path = path

    def load(self) -> List[Document]:
        documents = []

        reader = PdfReader(self.path)

        for index, page in enumerate(reader.pages):
            text = page.extract_text()

            if not text:
                continue

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": self.path,
                        "page": index + 1,
                        "type": "pdf",
                    },
                )
            )

        return documents
