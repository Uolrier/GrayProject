import re

from .chunker import BaseChunker
from .schema import Chunk


class MarkdownChunker(BaseChunker):
    """
    Split markdown text by heading structure.

    Supports:
    - h1 ~ h6 headings
    - fenced code block protection
    - section metadata
    """

    HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.*)$")

    def split(
        self,
        text: str,
    ) -> list[Chunk]:
        """
        Split markdown by headings.
        """

        sections = self._parse_sections(text)

        chunks = []

        for index, section in enumerate(sections):
            content = section["content"].strip()

            if not content:
                continue

            chunks.append(
                Chunk(
                    content=content,
                    metadata={
                        "chunk_id": index,
                        "section": section["title"],
                        "level": section["level"],
                    },
                )
            )

        return chunks

    def _parse_sections(
        self,
        text: str,
    ) -> list[dict]:
        """
        Parse markdown sections.
        """

        lines = text.splitlines()

        sections = []

        current_lines = []

        current_title = None
        current_level = 0

        in_code_block = False

        for line in lines:
            if line.strip().startswith("```"):
                in_code_block = not in_code_block

            heading = None

            if not in_code_block:
                match = self.HEADING_PATTERN.match(line)

                if match:
                    heading = (
                        len(match.group(1)),
                        match.group(2).strip(),
                    )

            if heading:
                if current_lines:
                    sections.append(
                        {
                            "title": current_title,
                            "level": current_level,
                            "content": "\n".join(current_lines),
                        }
                    )

                current_level, current_title = heading

                current_lines = [line]

            else:
                current_lines.append(line)

        if current_lines:
            sections.append(
                {
                    "title": current_title,
                    "level": current_level,
                    "content": "\n".join(current_lines),
                }
            )

        return sections
