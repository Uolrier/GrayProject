"""Tests for prompt builder debug integration."""

from backend.app.llm.debug import PromptDebugLogger
from backend.app.llm.prompts.builder import PromptBuilder


def test_prompt_builder_with_debug_logger():
    logger = PromptDebugLogger()

    builder = PromptBuilder()

    messages = builder.build(
        user_message="Explain RAG",
        debugger=logger,
    )

    record = logger.latest()

    assert record is not None
    assert record["messages"] == messages
    assert messages[-1]["content"] == "Explain RAG"
