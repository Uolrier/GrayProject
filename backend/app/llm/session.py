from dataclasses import dataclass, field

from backend.app.llm.schema import ChatMessage


@dataclass
class ChatSession:
    """
    聊天会话，负责维护多轮对话历史。
    """

    messages: list[ChatMessage] = field(default_factory=list)

    def add_user_message(self, content: str) -> None:
        """
        添加用户消息。
        """
        self.messages.append(
            ChatMessage(
                role="user",
                content=content,
            )
        )

    def add_assistant_message(self, content: str) -> None:
        """
        添加助手消息。
        """
        self.messages.append(
            ChatMessage(
                role="assistant",
                content=content,
            )
        )

    def add_system_message(self, content: str) -> None:
        """
        添加系统消息。
        """
        self.messages.append(
            ChatMessage(
                role="system",
                content=content,
            )
        )

    def get_messages(self) -> list[ChatMessage]:
        """
        获取当前会话中的所有消息。
        """
        return self.messages

    def clear(self) -> None:
        """
        清空聊天记录。
        """
        self.messages.clear()

    def last_message(self) -> ChatMessage | None:
        """
        获取最后一条消息。
        """
        if not self.messages:
            return None

        return self.messages[-1]

    def remove_last_assistant(self) -> bool:
        """
        删除最后一条 Assistant 消息。

        仅当当前会话最后一条消息为 assistant 时执行删除。

        Returns:
            bool: 删除成功返回 True，否则返回 False。
        """
        if not self.messages:
            return False

        if self.messages[-1].role != "assistant":
            return False

        self.messages.pop()
        return True
