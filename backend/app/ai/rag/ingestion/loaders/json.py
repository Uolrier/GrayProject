import json
from pathlib import Path

from ..base import BaseDocumentLoader
from ..schema import Document


class JSONDocumentLoader(BaseDocumentLoader):
    """
    JSON document loader.

    Supports:
    - object json
    - list json
    - primitive json values
    """

    def load(self, path: str) -> list[Document]:
        file_path = Path(path)

        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        return self._convert(data)

    def _convert(self, data) -> list[Document]:
        if isinstance(data, list):
            return [self._convert_item(item) for item in data]

        return [self._convert_item(data)]

    def _convert_item(self, item) -> Document:
        if isinstance(item, dict):
            # 优先处理 content 字段
            if "content" in item:
                metadata = {k: v for k, v in item.items() if k != "content"}

                return Document(page_content=str(item["content"]), metadata=metadata)

            # 普通 JSON object
            content = "\n".join(f"{k}: {v}" for k, v in item.items())

            return Document(page_content=content)

        return Document(page_content=str(item))
