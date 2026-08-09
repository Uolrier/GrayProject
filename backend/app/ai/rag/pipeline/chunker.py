from abc import ABC, abstractmethod
from typing import Iterator

from ..config import ChunkConfig
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

    def split_iter(self, text: str) -> Iterator[Chunk]:
        """
        Lazily split text into chunks.

        The default implementation preserves compatibility
        with existing chunkers.
        """
        yield from self.split(text)


class FixedLengthChunker(BaseChunker):
    """
    Split text into fixed-length chunks.
    """

    def __init__(
        self,
        chunk_size: int | None = None,
        config: ChunkConfig | None = None,
    ):
        if config:
            chunk_size = config.fixed_chunk_size

        if chunk_size is None:
            chunk_size = 500

        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than zero")

        self.chunk_size = chunk_size

    def split_iter(self, text: str) -> Iterator[Chunk]:
        start = 0
        chunk_id = 0
        text_length = len(text)

        while start < text_length:
            end = min(
                start + self.chunk_size,
                text_length,
            )

            yield Chunk(
                content=text[start:end],
                metadata={
                    "chunk_id": chunk_id,
                    "start": start,
                    "end": end,
                },
            )

            chunk_id += 1
            start = end

    def split(self, text: str) -> list[Chunk]:
        return list(self.split_iter(text))


class OverlapChunker(BaseChunker):
    """
    Split text using sliding window overlap.
    """

    def __init__(
        self,
        chunk_size: int | None = None,
        overlap: int | None = None,
        config: ChunkConfig | None = None,
    ):
        if config:
            chunk_size = config.overlap_chunk_size
            overlap = config.overlap

        if chunk_size is None:
            chunk_size = 500

        if overlap is None:
            overlap = 50

        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than zero")

        if overlap < 0:
            raise ValueError("overlap cannot be negative")

        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_iter(self, text: str) -> Iterator[Chunk]:
        start = 0
        chunk_id = 0
        text_length = len(text)

        while start < text_length:
            end = min(
                start + self.chunk_size,
                text_length,
            )

            yield Chunk(
                content=text[start:end],
                metadata={
                    "chunk_id": chunk_id,
                    "start": start,
                    "end": end,
                },
            )

            chunk_id += 1

            if end >= text_length:
                break

            start = end - self.overlap

    def split(self, text: str) -> list[Chunk]:
        return list(self.split_iter(text))
