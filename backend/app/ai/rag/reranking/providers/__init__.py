from ..registry import RerankerRegistry
from .bge import BGEReranker
from .cross_encoder import CrossEncoderReranker
from .dummy import DummyReranker

RerankerRegistry.register(
    "dummy",
    DummyReranker,
)

RerankerRegistry.register(
    "bge",
    BGEReranker,
)

RerankerRegistry.register(
    "cross_encoder",
    CrossEncoderReranker,
)


__all__ = [
    "DummyReranker",
    "BGEReranker",
    "CrossEncoderReranker",
]
