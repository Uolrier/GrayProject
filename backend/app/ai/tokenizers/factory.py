from .registry import TokenizerRegistry


class TokenizerFactory:
    """
    Tokenizer factory.
    """

    @staticmethod
    def create(
        name: str,
        **kwargs,
    ):
        tokenizer_cls = TokenizerRegistry.get(name)

        if tokenizer_cls is None:
            raise ValueError(f"Unknown tokenizer: {name}")

        return tokenizer_cls(**kwargs)
