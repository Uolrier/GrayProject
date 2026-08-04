from backend.app.ai.rag.pipeline.code_chunker import (
    CodeChunker,
)


def test_python_code_chunker_basic():
    code = """
class User:

    def create(self):
        pass


def main():
    pass
"""

    chunker = CodeChunker(
        language="python",
        chunk_size=200,
    )

    chunks = chunker.split(code)

    assert len(chunks) == 2

    assert "class User" in chunks[0].content
    assert "def main" in chunks[1].content

    assert chunks[0].metadata["language"] == "python"


def test_java_code_chunker_basic():
    code = """
public class User {

}


public void hello() {

}
"""

    chunker = CodeChunker(
        language="java",
        chunk_size=200,
    )

    chunks = chunker.split(code)

    assert len(chunks) >= 1

    assert chunks[0].metadata["language"] == "java"


def test_code_chunker_fallback():
    code = "a" * 1200

    chunker = CodeChunker(
        language="python",
        chunk_size=500,
    )

    chunks = chunker.split(code)

    assert len(chunks) == 3

    assert (
        chunks[0].metadata["type"] == "start"
        or chunks[0].metadata.get("type") == "code_block"
    )


def test_unsupported_language_fallback():
    code = "a" * 600

    chunker = CodeChunker(
        language="unknown",
        chunk_size=500,
    )

    chunks = chunker.split(code)

    assert len(chunks) == 2
