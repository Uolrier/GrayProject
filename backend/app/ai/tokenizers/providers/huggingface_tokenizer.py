from transformers import AutoTokenizer

from ..base import BaseTokenizer
from ..registry import TokenizerRegistry


@TokenizerRegistry.register("huggingface")
class HuggingFaceTokenizer(BaseTokenizer):
    name = "huggingface"

    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-0.5B-Instruct",
    ):
        self.model_name = model_name

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def encode(
        self,
        text: str,
    ) -> list[int]:
        return self.tokenizer.encode(
            text,
            add_special_tokens=False,
        )

    def decode(
        self,
        tokens: list[int],
    ) -> str:
        return self.tokenizer.decode(tokens)

    def count_tokens(
        self,
        text: str,
    ) -> int:
        return len(self.encode(text))
