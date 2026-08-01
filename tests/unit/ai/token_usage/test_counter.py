from unittest.mock import MagicMock

from backend.app.ai.token_usage.counter import TokenCounter


def test_token_counter():
    manager = MagicMock()

    tokenizer = MagicMock()

    tokenizer.encode.return_value = [
        1,
        2,
        3,
    ]

    manager.get.return_value = tokenizer

    counter = TokenCounter(manager)

    result = counter.count(
        "hello",
        "gpt-4",
    )

    assert result == 3

    manager.get.assert_called_once_with("gpt-4")
