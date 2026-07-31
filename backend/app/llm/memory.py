from typing import Dict, List

from .schema import ChatMessage


class ConversationMemory:
    """
    多轮对话历史管理

    当前版本:
    - 内存存储
    - 进程级生命周期

    后续可替换:
    - Redis
    - SQLite
    - PostgreSQL
    """

    def __init__(self):
        self.sessions: Dict[str, List[ChatMessage]] = {}

    def add_message(
        self,
        session_id: str,
        message: ChatMessage,
    ) -> None:
        """
        添加消息
        """

        if session_id not in self.sessions:
            self.sessions[session_id] = []

        self.sessions[session_id].append(message)

    def get_history(
        self,
        session_id: str,
    ) -> List[ChatMessage]:
        """
        获取历史消息
        """

        return self.sessions.get(
            session_id,
            [],
        )

    def clear_session(
        self,
        session_id: str,
    ) -> None:
        """
        清除指定会话
        """

        self.sessions.pop(
            session_id,
            None,
        )

    def clear_all(self) -> None:
        """
        清除所有会话
        """

        self.sessions.clear()
