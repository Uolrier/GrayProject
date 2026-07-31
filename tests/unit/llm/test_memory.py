from backend.app.llm.memory import ConversationMemory
from backend.app.llm.schema import ChatMessage


def test_memory_add_and_get():
    memory = ConversationMemory()

    message = ChatMessage(
        role="user",
        content="你好",
    )

    memory.add_message(
        "session_001",
        message,
    )

    history = memory.get_history(
        "session_001",
    )

    assert len(history) == 1

    assert history[0].content == "你好"


def test_memory_session_isolation():
    memory = ConversationMemory()

    memory.add_message(
        "A",
        ChatMessage(
            role="user",
            content="我是A",
        ),
    )

    memory.add_message(
        "B",
        ChatMessage(
            role="user",
            content="我是B",
        ),
    )

    assert memory.get_history("A")[0].content == "我是A"

    assert memory.get_history("B")[0].content == "我是B"
