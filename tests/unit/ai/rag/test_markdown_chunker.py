from backend.app.ai.rag.pipeline.markdown_chunker import (
    MarkdownChunker,
)


def test_markdown_heading_split():
    text = """
# Title

hello

## Install

pip install gray
"""

    chunker = MarkdownChunker()

    chunks = chunker.split(text)

    assert len(chunks) == 2

    assert chunks[0].metadata["section"] == "Title"
    assert chunks[0].metadata["level"] == 1

    assert chunks[1].metadata["section"] == "Install"
    assert chunks[1].metadata["level"] == 2


def test_markdown_multi_level_heading():
    text = """
# A

## B

### C
"""

    chunker = MarkdownChunker()

    chunks = chunker.split(text)

    assert len(chunks) == 3

    assert chunks[0].metadata["level"] == 1
    assert chunks[1].metadata["level"] == 2
    assert chunks[2].metadata["level"] == 3


def test_markdown_code_block_should_not_split():
    text = (
        "# Python\n\n"
        "```python\n"
        "# fake heading\n"
        'print("hello")\n'
        "```\n\n"
        "## Result\n\n"
        "done\n"
    )

    chunker = MarkdownChunker()

    chunks = chunker.split(text)

    assert len(chunks) == 2

    assert chunks[0].metadata["section"] == "Python"
    assert chunks[1].metadata["section"] == "Result"
