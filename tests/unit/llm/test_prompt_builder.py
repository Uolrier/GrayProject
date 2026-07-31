"""Tests for LLM PromptBuilder."""

from backend.app.llm.prompts import PromptBuilder


def test_default_system_prompt():
    builder = PromptBuilder()

    messages = builder.build(
        "hello",
    )

    assert messages[0]["role"] == "system"
    assert "GrayProject" in messages[0]["content"]


def test_history_injection():
    builder = PromptBuilder()

    history = [
        {
            "role": "user",
            "content": "old question",
        },
        {
            "role": "assistant",
            "content": "old answer",
        },
    ]

    messages = builder.build(
        "new question",
        history=history,
    )

    assert len(messages) == 4
    assert messages[1]["content"] == "old question"
    assert messages[2]["content"] == "old answer"


def test_context_injection():
    builder = PromptBuilder()

    messages = builder.build(
        "question",
        context="knowledge",
    )

    assert len(messages) == 3
    assert "knowledge" in messages[1]["content"]


def test_custom_system_prompt():
    builder = PromptBuilder(
        system_prompt="custom prompt",
    )

    messages = builder.build(
        "hello",
    )

    assert messages[0]["content"] == "custom prompt"
