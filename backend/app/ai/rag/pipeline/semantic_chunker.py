import re

from .chunker import BaseChunker
from .schema import Chunk


class SemanticChunker(BaseChunker):
    """
    Split text based on semantic similarity.

    Current implementation:
        - sentence based splitting
        - word overlap similarity

    Future:
        replace similarity with embedding similarity.
    """

    def __init__(
        self,
        similarity_threshold: float = 0.3,
        max_chunk_size: int = 500,
    ):
        if not 0 <= similarity_threshold <= 1:
            raise ValueError("similarity_threshold must be between 0 and 1")

        if max_chunk_size <= 0:
            raise ValueError("max_chunk_size must be greater than zero")

        self.similarity_threshold = similarity_threshold
        self.max_chunk_size = max_chunk_size

    def split(
        self,
        text: str,
    ) -> list[Chunk]:
        sentences = self._split_sentences(text)

        if not sentences:
            return []

        groups = self._merge_sentences(sentences)

        chunks = []

        for index, group in enumerate(groups):
            chunks.append(
                Chunk(
                    content="\n".join(group),
                    metadata={
                        "chunk_id": index,
                        "type": "semantic",
                    },
                )
            )

        return chunks

    def _split_sentences(
        self,
        text: str,
    ) -> list[str]:
        sentences = re.split(
            r"(?<=[。！？.!?])\s*",
            text.strip(),
        )

        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def _merge_sentences(
        self,
        sentences: list[str],
    ) -> list[list[str]]:
        groups = []

        current = []

        current_length = 0

        for sentence in sentences:
            if not current:
                current.append(sentence)
                current_length += len(sentence)
                continue

            similarity = self._similarity(
                current[-1],
                sentence,
            )

            if (
                similarity >= self.similarity_threshold
                and current_length + len(sentence) <= self.max_chunk_size
            ):
                current.append(sentence)
                current_length += len(sentence)

            else:
                groups.append(current)

                current = [sentence]
                current_length = len(sentence)

        if current:
            groups.append(current)

        return groups

    def _similarity(
        self,
        a: str,
        b: str,
    ) -> float:
        """
        Calculate word overlap similarity.

        Placeholder for embedding similarity.
        """

        words_a = set(self._tokenize(a))
        words_b = set(self._tokenize(b))

        if not words_a or not words_b:
            return 0.0

        return len(words_a & words_b) / len(words_a | words_b)

    def _tokenize(
        self,
        text: str,
    ) -> list[str]:
        tokens = []

        tokens.extend(
            re.findall(
                r"[A-Za-z0-9_]+",
                text,
            )
        )

        tokens.extend(
            re.findall(
                r"[\u4e00-\u9fff]{2,}",
                text,
            )
        )

        return tokens
