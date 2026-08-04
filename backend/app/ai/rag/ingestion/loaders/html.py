from pathlib import Path
from typing import List

from bs4 import BeautifulSoup

from ..base import BaseDocumentLoader
from ..factory import LoaderFactory
from ..schema import Document


@LoaderFactory.register("html")
@LoaderFactory.register("htm")
class HTMLLoader(BaseDocumentLoader):
    """
    Loader for HTML documents.
    """

    def __init__(self, path: str):
        self.path = Path(path)

    def load(self) -> List[Document]:
        """
        Load HTML file and extract plain text.
        """

        if not self.path.exists():
            raise FileNotFoundError(self.path)

        html = self.path.read_text(encoding="utf-8")

        soup = BeautifulSoup(html, "html.parser")

        # Remove non-content elements
        for tag in soup(["script", "style"]):
            tag.decompose()

        content = soup.get_text(
            separator="\n",
            strip=True,
        )

        return [
            Document(
                page_content=content,
                metadata={
                    "source": str(self.path),
                    "type": "html",
                },
            )
        ]
