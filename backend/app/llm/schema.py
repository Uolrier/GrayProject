from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ChatMessage:
    """
    单条聊天消息
    """

    role: str
    content: str


@dataclass
class ChatRequest:
    """
    LLM聊天请求协议
    """

    session_id: Optional[str] = None

    messages: List[ChatMessage] = field(default_factory=list)

    system_prompt: Optional[str] = None

    model: Optional[str] = None

    temperature: float = 0.7

    max_tokens: Optional[int] = None

    stream: bool = False

    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TokenUsage:
    """
    Token使用统计
    """

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0


@dataclass
class ChatResponse:
    """
    LLM聊天响应协议
    """

    content: str

    model: Optional[str] = None

    provider: Optional[str] = None

    usage: Optional[TokenUsage] = None

    metadata: Dict[str, Any] = field(default_factory=dict)
