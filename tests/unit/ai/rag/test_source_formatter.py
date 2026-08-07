from backend.app.ai.rag.source.formatter import SourceFormatter
from backend.app.ai.rag.source.schema import SourceReference


def test_source_formatter():
    formatter = SourceFormatter()

    sources = [
        SourceReference(
            file_path="README.md",
            chunk_id="1",
            score=0.92,
        ),
        SourceReference(
            file_path="docs/test.md",
            chunk_id="2",
            score=0.88,
        ),
    ]

    result = formatter.format(
        sources,
    )

    assert "[1] README.md" in result

    assert "[2] docs/test.md" in result

    assert "0.920" in result

    assert "0.880" in result
