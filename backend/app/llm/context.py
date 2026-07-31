from typing import List

from .schema import ChatMessage
from .session import ChatSession


class ContextBuilder:
    """
    根据聊天Session构造LLM上下文
    """

    def build(
        self,
        session: ChatSession,
        system_prompt: str | None = None,
    ) -> List[ChatMessage]:
        messages = []

        if system_prompt:
            messages.append(
                ChatMessage(
                    role="system",
                    content=system_prompt,
                )
            )

        messages.extend(session.get_messages())

        return messages
