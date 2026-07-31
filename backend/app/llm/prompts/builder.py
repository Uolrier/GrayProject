"""Prompt builder for constructing LLM messages."""

from backend.app.llm.prompts.templates import DEFAULT_SYSTEM_PROMPT


class PromptBuilder:
    """Build structured messages for LLM requests."""

    def __init__(
        self,
        system_prompt: str | None = None,
    ):
        self.system_prompt = system_prompt or DEFAULT_SYSTEM_PROMPT

    def build(
        self,
        user_message: str,
        history: list[dict] | None = None,
        context: str | None = None,
    ) -> list[dict]:
        """Build message list for LLM input."""

        messages = [
            {
                "role": "system",
                "content": self.system_prompt.strip(),
            }
        ]

        if history:
            messages.extend(history)

        if context:
            messages.append(
                {
                    "role": "system",
                    "content": (f"Context:\n{context}"),
                }
            )

        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        return messages
