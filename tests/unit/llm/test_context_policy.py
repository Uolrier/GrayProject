from backend.app.llm.context_policy import ContextPolicy


def test_available_tokens():
    policy = ContextPolicy(
        max_tokens=4096,
        reserve_tokens=1000,
    )

    assert policy.available_tokens == 3096
