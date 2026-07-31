from backend.app.llm.schema import (
    ChatMessage,
    ChatRequest,
)


def test_system_prompt_should_be_supported():
    request = ChatRequest(
        system_prompt="You are a Python expert.",
        messages=[ChatMessage(role="user", content="Explain decorator.")],
    )

    assert request.system_prompt == "You are a Python expert."


def test_system_prompt_order():
    messages = []

    request = ChatRequest(
        system_prompt="You are a Python expert.",
        messages=[ChatMessage(role="user", content="Explain decorator.")],
    )

    if request.system_prompt:
        messages.append(
            {
                "role": "system",
                "content": request.system_prompt,
            }
        )

    messages.extend(
        [
            {
                "role": msg.role,
                "content": msg.content,
            }
            for msg in request.messages
        ]
    )

    assert messages[0]["role"] == "system"

    assert messages[0]["content"] == ("You are a Python expert.")

    assert messages[1]["role"] == "user"
