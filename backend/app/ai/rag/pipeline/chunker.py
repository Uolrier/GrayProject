from abc import ABC, abstractmethod

from .schema import Chunk


class BaseChunker(ABC):
    """
    Base interface for document chunkers.
    """

    @abstractmethod
    def split(self, text: str) -> list[Chunk]:
        """
        Split text into chunks.
        """
        pass


class FixedLengthChunker(BaseChunker):
    """
    Split text into fixed-length chunks.

    Args:
        chunk_size:
            Maximum length of each chunk.

        overlap:
            Number of overlapping characters between chunks.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50,
    ):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than zero")

        if overlap < 0:
            raise ValueError("overlap cannot be negative")

        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text: str) -> list[Chunk]:
        """
        Split text using sliding window.

        Example:

            chunk_size=10
            overlap=2

            0123456789ABCDEFGHIJ

            =>
            0123456789
            89ABCDEFGH
            GHIJ
        """

        chunks = []

        start = 0
        chunk_id = 0

        text_length = len(text)

        while start < text_length:
            end = min(
                start + self.chunk_size,
                text_length,
            )

            chunk_text = text[start:end]

            chunks.append(
                Chunk(
                    content=chunk_text,
                    metadata={
                        "chunk_id": chunk_id,
                        "start": start,
                        "end": end,
                    },
                )
            )

            chunk_id += 1

            # 最后一个 chunk 结束，退出循环
            if end >= text_length:
                break

            start = end - self.overlap

        return chunks
