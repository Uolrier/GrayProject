from backend.app.ai.token_usage.schema import TokenUsage


def test_token_usage_total():
    usage = TokenUsage(
        prompt_tokens=10,
        completion_tokens=20,
    )

    assert usage.total_tokens == 30
