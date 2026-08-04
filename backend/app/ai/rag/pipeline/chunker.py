from typing import List


class TextChunker:
    """
    Simple text splitter.

    Later can be replaced by:
    - token based splitter
    - markdown splitter
    - semantic splitter
    """

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50,
    ):
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text: str) -> List[str]:
        if not text:
            return []

        chunks = []

        start = 0

        while start < len(text):
            end = start + self.chunk_size

            chunks.append(text[start:end])

            start += self.chunk_size - self.overlap

        return chunks
