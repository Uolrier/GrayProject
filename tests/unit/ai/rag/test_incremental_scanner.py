from pathlib import Path

from backend.app.ai.rag.incremental.scanner import FileScanner


def test_file_scanner(tmp_path: Path):
    file1 = tmp_path / "a.txt"

    file1.write_text(
        "hello",
        encoding="utf-8",
    )

    scanner = FileScanner(str(tmp_path))

    result = scanner.scan()

    assert "a.txt" in result

    state = result["a.txt"]

    assert state.size == 5

    assert state.hash is not None
