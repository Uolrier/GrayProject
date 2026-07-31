"""Tests for LLM prompt debug utilities."""

from backend.app.llm.debug import (
    PromptDebugLogger,
    format_messages,
)


def test_prompt_debug_logger_store():
    logger = PromptDebugLogger()

    record = logger.log(
        messages=[
            {
                "role": "user",
                "content": "hello",
            }
        ],
        model="deepseek",
    )

    assert record["model"] == "deepseek"
    assert record["messages"][0]["content"] == "hello"


def test_prompt_debug_logger_latest():
    logger = PromptDebugLogger()

    logger.log(
        messages=[
            {
                "role": "user",
                "content": "first",
            }
        ]
    )

    logger.log(
        messages=[
            {
                "role": "user",
                "content": "second",
            }
        ]
    )

    latest = logger.latest()

    assert latest["messages"][0]["content"] == "second"


def test_format_messages():
    result = format_messages(
        [
            {
                "role": "system",
                "content": "You are Gray AI",
            },
            {
                "role": "user",
                "content": "Explain RAG",
            },
        ]
    )

    assert "SYSTEM" in result
    assert "USER" in result
    assert "Explain RAG" in result
