"""
LLM Provider Registry

负责管理所有 LLM Provider 的注册与获取。
"""

from typing import Dict, Type

from .base import BaseLLM

PROVIDERS: Dict[str, Type[BaseLLM]] = {}


def register_provider(name: str):
    """
    注册 LLM Provider。

    Example:

        @register_provider("deepseek")
        class DeepSeekLLM(BaseLLM):
            pass
    """

    def decorator(cls: Type[BaseLLM]):
        PROVIDERS[name] = cls
        return cls

    return decorator


def get_provider(name: str) -> Type[BaseLLM]:
    """
    获取 Provider 类。
    """

    if name not in PROVIDERS:
        raise ValueError(f"Unknown LLM provider: {name}")

    return PROVIDERS[name]
