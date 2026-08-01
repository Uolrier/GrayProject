from typing import List

from .schema import ChatMessage


class ContextManager:
    """
    控制LLM上下文长度
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
        计算消息token数量
        """

        text = "\n".join(message.content for message in messages)

        return self.tokenizer.count(text)

    def fit(
        self,
        messages: List[ChatMessage],
    ) -> List[ChatMessage]:
        """
        根据context限制裁剪消息
        """

        messages = list(messages)

        system_message = None

        # 保留system prompt
        if messages and messages[0].role == "system":
            system_message = messages.pop(0)

        while self.count_tokens(messages) > self.policy.available_tokens:
            if not messages:
                break

            # 删除最早历史消息
            messages.pop(0)

        if system_message:
            messages.insert(
                0,
                system_message,
            )

        return messages
