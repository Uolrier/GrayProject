from .base import BaseRuntime
from .dummy import DummyRuntime
from .factory import RuntimeFactory
from .huggingface import HuggingFaceRuntime
from .registry import RuntimeRegistry

RuntimeRegistry.register(
    "dummy",
    DummyRuntime,
)

RuntimeRegistry.register(
    "huggingface",
    HuggingFaceRuntime,
)

__all__ = [
    "BaseRuntime",
    "DummyRuntime",
    "HuggingFaceRuntime",
    "RuntimeRegistry",
    "RuntimeFactory",
]
