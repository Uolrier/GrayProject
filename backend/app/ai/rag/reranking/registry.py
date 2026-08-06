from .base import BaseReranker


class RerankerRegistry:
    _providers: dict[str, type[BaseReranker]] = {}

    @classmethod
    def register(
        cls,
        name: str,
        provider: type[BaseReranker],
    ):
        cls._providers[name] = provider

    @classmethod
    def get(
        cls,
        name: str,
    ):
        return cls._providers[name]

    @classmethod
    def available(cls):
        return list(cls._providers.keys())
