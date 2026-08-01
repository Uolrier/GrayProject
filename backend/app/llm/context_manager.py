from typing import List

from .schema import ChatMessage


class ContextManager:
    """
    控制 LLM 上下文长度。

    负责：
    - token 统计
    - context 自动截断
    - system message 保护
    """

    def __init__(
        self,
        tokenizer,
        policy,
    ):
        self.tokenizer = tokenizer
        self.policy = policy

    def count_tokens(
        self,
        messages: List[ChatMessage],
    ) -> int:
        """
        计算消息 token 数量。
        """

        text = "\n".join(message.content for message in messages)

        return self.tokenizer.count(text)

    def fit(
        self,
        messages: List[ChatMessage],
    ) -> List[ChatMessage]:
        """
        根据 context 限制裁剪消息。

        策略：
        1. system message 永久保留
        2. 优先删除最旧历史消息
        3. user/assistant 成对删除，避免上下文断裂
        """

        messages = list(messages)

        system_messages = []
        history_messages = []

        # 分离 system 与历史消息
        for message in messages:
            if message.role == "system":
                system_messages.append(message)
            else:
                history_messages.append(message)

        # 删除旧历史，直到满足限制
        while (
            self.count_tokens(system_messages + history_messages)
            > self.policy.available_tokens
        ):
            if not history_messages:
                break

            self._remove_oldest_turn(history_messages)

        return system_messages + history_messages

    def _remove_oldest_turn(
        self,
        messages: List[ChatMessage],
    ) -> None:
        """
        删除最早的一轮对话。

        优先删除：
        user
        assistant

        如果只有单条消息，则删除单条。
        """

        if not messages:
            return

        # 删除第一条消息
        first = messages.pop(0)

        # 如果第一条是 user，
        # 同时删除紧随其后的 assistant
        if first.role == "user" and messages and messages[0].role == "assistant":
            messages.pop(0)
