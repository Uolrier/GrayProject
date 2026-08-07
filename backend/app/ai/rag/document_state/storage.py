import json
from pathlib import Path
from typing import Any, Dict


class DocumentStateStorage:
    def __init__(self, path: str):
        self.path = Path(path)

    def load(self) -> Dict[str, Any]:
        if not self.path.exists():
            return {}

        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self, data: Dict[str, Any]):
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.path.write_text(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
