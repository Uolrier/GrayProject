from backend.app.ai.tokenizers.manager import TokenizerManager


class TokenCounter:
    def __init__(
        self,
        tokenizer_manager: TokenizerManager,
    ):
        self.tokenizer_manager = tokenizer_manager

    def count(
        self,
        text: str,
        tokenizer_name: str,
    ) -> int:
        tokenizer = self.tokenizer_manager.get(tokenizer_name)

        return len(tokenizer.encode(text))
