from dataclasses import dataclass


@dataclass
class ContextPolicy:
    """
    Context window control configuration.
    """

    max_tokens: int

    reserve_tokens: int = 1000

    strategy: str = "truncate"

    @property
    def available_tokens(self) -> int:
        return max(
            self.max_tokens - self.reserve_tokens,
            0,
        )
