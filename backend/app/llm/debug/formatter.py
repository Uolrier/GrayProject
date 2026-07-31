"""Prompt formatting utilities."""

from typing import Any


def format_messages(
    messages: list[dict[str, Any]],
) -> str:
    """
    Format LLM messages into readable debug text.
    """

    sections = []

    for message in messages:
        role = message.get("role", "unknown").upper()
        content = message.get("content", "")

        sections.append(f"========== {role} ==========\n\n{content}")

    return "\n\n".join(sections)
