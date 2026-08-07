from typing import List

from .base import BaseContextBuilder
from .formatter import ContextFormatter
from .schema import BuiltContext, ContextChunk


class SimpleContextBuilder(BaseContextBuilder):
    """
    Basic context assembly strategy.
    """

    def __init__(
        self,
        max_chunks: int = 5,
    ):
        self.max_chunks = max_chunks
        self.formatter = ContextFormatter()

    def build(
        self,
        chunks: List[ContextChunk],
    ) -> BuiltContext:
        selected_chunks = chunks[: self.max_chunks]

        formatted_chunks = []

        for chunk in selected_chunks:
            formatted_chunks.append(self.formatter.format(chunk))

        context_text = "\n\n---\n\n".join(formatted_chunks)

        return BuiltContext(
            text=context_text,
            chunks=selected_chunks,
        )
