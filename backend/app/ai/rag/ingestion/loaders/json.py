import json
from pathlib import Path

from ..base import BaseDocumentLoader
from ..factory import LoaderFactory
from ..schema import Document


@LoaderFactory.register("json")
class JSONDocumentLoader(BaseDocumentLoader):
    def __init__(self, path: str | None = None):
        self.path = Path(path) if path else None

    def load(self, path: str | None = None):
        file_path = Path(path) if path else self.path

        if file_path is None:
            raise ValueError("path required")

        with file_path.open(
            "r",
            encoding="utf-8",
        ) as f:
            data = json.load(f)

        return self._convert(data)

    def _convert(self, data):
        if isinstance(data, list):
            return [self._convert_item(item) for item in data]

        return [self._convert_item(data)]

    def _convert_item(self, item):
        if isinstance(item, dict):
            if "content" in item:
                metadata = {k: v for k, v in item.items() if k != "content"}

                return Document(
                    page_content=str(item["content"]),
                    metadata=metadata,
                )

            content = "\n".join(f"{k}: {v}" for k, v in item.items())

            return Document(page_content=content)

        return Document(page_content=str(item))
