from pathlib import Path

from backend.app.ai.rag.incremental.loader_adapter import (
    DocumentLoaderAdapter,
)


def test_loader_adapter(tmp_path: Path):
    file = tmp_path / "test.md"

    file.write_text(
        "# hello",
        encoding="utf-8",
    )

    adapter = DocumentLoaderAdapter()

    docs = adapter.load(str(file))

    assert len(docs) == 1

    assert docs[0].page_content == "# hello"

    assert docs[0].metadata["type"] == "markdown"
