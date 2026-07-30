from backend.app.llm.schema import (
    ChatResponse,
    TokenUsage,
)


def test_chat_response():
    response = ChatResponse(
        content="hello",
        model="deepseek-chat",
        provider="deepseek",
    )

    assert response.content == "hello"
    assert response.model == "deepseek-chat"
    assert response.provider == "deepseek"


def test_token_usage():
    usage = TokenUsage(
        prompt_tokens=10,
        completion_tokens=20,
        total_tokens=30,
    )

    assert usage.prompt_tokens == 10
    assert usage.completion_tokens == 20
    assert usage.total_tokens == 30
