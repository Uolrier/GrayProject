from ..registry import RerankerRegistry
from .bge import BGEReranker
from .dummy import DummyReranker

RerankerRegistry.register(
    "dummy",
    DummyReranker,
)

RerankerRegistry.register(
    "bge",
    BGEReranker,
)

__all__ = [
    "DummyReranker",
    "BGEReranker",
]
