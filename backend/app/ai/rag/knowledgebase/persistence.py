from __future__ import annotations

import json
from pathlib import Path

from .schema import KnowledgeBaseConfig


class KnowledgeBasePersistence:
    """
    Persist knowledge base configurations.
    """

    def __init__(
        self,
        path: str | Path = ".gray/knowledge_bases.json",
    ):
        self.path = Path(path)

    def load(self) -> list[KnowledgeBaseConfig]:
        if not self.path.exists():
            return []

        data = json.loads(self.path.read_text(encoding="utf-8"))

        return [KnowledgeBaseConfig(**item) for item in data.get("knowledge_bases", [])]

    def save(
        self,
        configs: list[KnowledgeBaseConfig],
    ) -> None:
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        data = {
            "knowledge_bases": [
                {
                    "name": config.name,
                    "type": config.type,
                    "embedding": config.embedding,
                    "vectordb": config.vectordb,
                    "reranker": config.reranker,
                    "metadata": config.metadata,
                    "root_path": config.root_path,
                    "auto_update": config.auto_update,
                    "watch_interval": config.watch_interval,
                }
                for config in configs
            ]
        }

        self.path.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
