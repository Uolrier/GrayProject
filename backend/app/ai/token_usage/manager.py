from .counter import TokenCounter
from .schema import TokenUsage


class TokenUsageManager:
    def __init__(
        self,
        counter: TokenCounter,
    ):
        self.counter = counter

    def calculate(
        self,
        prompt: str,
        completion: str,
        tokenizer_name: str,
    ) -> TokenUsage:
        return TokenUsage(
            prompt_tokens=self.counter.count(
                prompt,
                tokenizer_name,
            ),
            completion_tokens=self.counter.count(
                completion,
                tokenizer_name,
            ),
        )
