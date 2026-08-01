from unittest.mock import MagicMock

from backend.app.ai.token_usage.manager import TokenUsageManager


def test_token_usage_manager():
    counter = MagicMock()

    counter.count.side_effect = [
        10,
        20,
    ]

    manager = TokenUsageManager(counter)

    usage = manager.calculate(
        "prompt",
        "completion",
        "gpt-4",
    )

    assert usage.prompt_tokens == 10
    assert usage.completion_tokens == 20
    assert usage.total_tokens == 30
