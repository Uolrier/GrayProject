from backend.app.llm.context_manager import ContextManager
from backend.app.llm.context_policy import ContextPolicy
from backend.app.llm.schema import ChatMessage


class DummyTokenizer:
    def count(self, text):
        return len(text.split())


def create_manager(max_tokens):
    return ContextManager(
        tokenizer=DummyTokenizer(),
        policy=ContextPolicy(
            max_tokens=max_tokens,
            reserve_tokens=0,
        ),
    )


def test_truncation_removes_old_conversation_turn():
    manager = create_manager(
        max_tokens=5,
    )

    messages = [
        ChatMessage(
            role="user",
            content="one two three",
        ),
        ChatMessage(
            role="assistant",
            content="four five",
        ),
        ChatMessage(
            role="user",
            content="six seven",
        ),
    ]

    result = manager.fit(messages)

    roles = [message.role for message in result]

    contents = [message.content for message in result]

    assert roles == [
        "user",
    ]

    assert contents == [
        "six seven",
    ]


def test_system_message_always_preserved():
    manager = create_manager(
        max_tokens=3,
    )

    messages = [
        ChatMessage(
            role="system",
            content="system",
        ),
        ChatMessage(
            role="user",
            content="one two three",
        ),
        ChatMessage(
            role="assistant",
            content="four five six",
        ),
    ]

    result = manager.fit(messages)

    assert result[0].role == "system"


def test_multiple_system_messages_preserved():
    manager = create_manager(
        max_tokens=5,
    )

    messages = [
        ChatMessage(
            role="system",
            content="system one",
        ),
        ChatMessage(
            role="system",
            content="system two",
        ),
        ChatMessage(
            role="user",
            content="one two three",
        ),
    ]

    result = manager.fit(messages)

    assert result[0].role == "system"
    assert result[1].role == "system"


def test_empty_messages():
    manager = create_manager(
        max_tokens=5,
    )

    result = manager.fit([])

    assert result == []
