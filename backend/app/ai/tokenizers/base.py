from abc import ABC, abstractmethod


class BaseTokenizer(ABC):
    """
    Base tokenizer interface.
    """

    name: str = "base"

    @abstractmethod
    def encode(
        self,
        text: str,
    ) -> list[int]:
        """
        Encode text into token ids.
        """

    @abstractmethod
    def decode(
        self,
        tokens: list[int],
    ) -> str:
        """
        Decode token ids into text.
        """

    @abstractmethod
    def count_tokens(
        self,
        text: str,
    ) -> int:
        """
        Count tokens.
        """
