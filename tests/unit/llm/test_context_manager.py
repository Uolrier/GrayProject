from backend.app.llm.context_manager import ContextManager
from backend.app.llm.context_policy import ContextPolicy
from backend.app.llm.schema import ChatMessage


class DummyTokenizer:
    def count(self, text):
        return len(text.split())


def test_context_trim():
    manager = ContextManager(
        tokenizer=DummyTokenizer(),
        policy=ContextPolicy(
            max_tokens=5,
            reserve_tokens=0,
        ),
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

    assert manager.count_tokens(result) <= 5
