from dataclasses import dataclass


@dataclass(slots=True)
class StreamChunk:
    """
    A single chunk produced during streaming generation.
    """

    content: str
    finished: bool = False
    finish_reason: str | None = None
