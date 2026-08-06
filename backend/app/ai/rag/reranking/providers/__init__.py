from ..registry import RerankerRegistry
from .dummy import DummyReranker

RerankerRegistry.register(
    "dummy",
    DummyReranker,
)

__all__ = [
    "DummyReranker",
]
