import re

from ..config import ChunkConfig
from .chunker import BaseChunker, FixedLengthChunker
from .schema import Chunk


class CodeChunker(BaseChunker):
    """
    Split source code into logical chunks.

    Supports:
        - Python
        - Java
        - C/C++
        - JavaScript

    Strategy:
        1. Split by class/function boundaries.
        2. Fallback to fixed length chunking.
    """

    def __init__(
        self,
        language: str,
        chunk_size: int = 500,
        config: ChunkConfig | None = None,
    ):
        if config:
            chunk_size = config.code_chunk_size
        self.language = language.lower()

        self.fallback_chunker = FixedLengthChunker(
            chunk_size=chunk_size,
        )

    def split(
        self,
        text: str,
    ) -> list[Chunk]:
        blocks = self._split_code_blocks(text)

        if not blocks:
            return self.fallback_chunker.split(text)

        chunks = []

        for index, block in enumerate(blocks):
            if len(block) <= self.fallback_chunker.chunk_size:
                chunks.append(
                    Chunk(
                        content=block,
                        metadata={
                            "chunk_id": index,
                            "type": "code_block",
                            "language": self.language,
                        },
                    )
                )
            else:
                sub_chunks = self.fallback_chunker.split(block)

                for sub in sub_chunks:
                    sub.metadata.update(
                        {
                            "type": "code_block",
                            "language": self.language,
                        }
                    )

                chunks.extend(sub_chunks)

        return chunks

    def _split_code_blocks(
        self,
        text: str,
    ) -> list[str]:
        if self.language == "python":
            return self._split_python(text)

        if self.language in {
            "java",
            "cpp",
            "c",
            "javascript",
            "js",
        }:
            return self._split_brace_language(text)

        return []

    def _split_python(
        self,
        text: str,
    ) -> list[str]:
        pattern = r"(?=^(?:class |def ))"

        blocks = re.split(
            pattern,
            text,
            flags=re.MULTILINE,
        )

        blocks = self._merge_python_blocks(blocks)

        return [block.strip() for block in blocks if block.strip()]

    def _merge_python_blocks(
        self,
        blocks: list[str],
    ) -> list[str]:
        result = []

        buffer = ""

        for block in blocks:
            if block.startswith(
                (
                    "class ",
                    "def ",
                )
            ):
                if buffer:
                    result.append(buffer)

                buffer = block
            else:
                buffer += block

        if buffer:
            result.append(buffer)

        return [item.strip() for item in result if item.strip()]

    def _split_brace_language(
        self,
        text: str,
    ) -> list[str]:
        pattern = (
            r"(?="
            r"(?:"
            r"class\s+\w+"
            r"|"
            r"(?:public|private|protected)?"
            r"\s*(?:static\s+)?"
            r"\w+\s+\w+\s*\("
            r")"
            r")"
        )

        blocks = re.split(
            pattern,
            text,
            flags=re.MULTILINE,
        )

        return [block.strip() for block in blocks if block.strip()]
