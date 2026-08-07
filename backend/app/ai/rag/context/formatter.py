from .schema import ContextChunk


class ContextFormatter:
    """
    Format retrieved chunks into LLM readable text.
    """

    def format(
        self,
        chunk: ContextChunk,
    ) -> str:
        source = chunk.metadata.get(
            "source",
            "unknown",
        )

        return f"[Source: {source}]\n\n{chunk.content}"
