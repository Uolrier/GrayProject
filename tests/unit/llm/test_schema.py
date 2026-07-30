from backend.app.llm.schema import ChatMessage, ChatRequest


def test_chat_message():
    message = ChatMessage(role="user", content="hello")

    assert message.role == "user"
    assert message.content == "hello"


def test_chat_request():
    request = ChatRequest(
        messages=[ChatMessage(role="user", content="hello")], model="deepseek-chat"
    )

    assert len(request.messages) == 1
    assert request.model == "deepseek-chat"
    assert request.temperature == 0.7
