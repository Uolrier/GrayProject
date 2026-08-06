from .registry import RerankerRegistry


class RerankerFactory:
    @staticmethod
    def create(
        name: str,
        **kwargs,
    ):
        provider = RerankerRegistry.get(name)

        return provider(**kwargs)
