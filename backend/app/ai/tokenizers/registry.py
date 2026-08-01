from backend.app.core.registry import Registry

from .base import BaseTokenizer

TokenizerRegistry = Registry[BaseTokenizer]()
