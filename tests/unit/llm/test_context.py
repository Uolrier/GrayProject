from backend.app.llm.context import ContextBuilder
from backend.app.llm.session import ChatSession


def test_context_builder():
    session = ChatSession()

    session.add_user_message("什么是RAG?")

    session.add_assistant_message("RAG是检索增强生成")

    builder = ContextBuilder()

    result = builder.build(
        session,
        "你是GrayProject AI",
    )

    assert len(result) == 3

    assert result[0].role == "system"

    assert result[0].content == "你是GrayProject AI"

    assert result[-1].content == "RAG是检索增强生成"
