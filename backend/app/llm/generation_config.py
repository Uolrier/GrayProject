from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional


@dataclass
class GenerationConfig:
    """
    LLM generation parameters.
    """

    temperature: float = 0.7

    max_tokens: Optional[int] = 2048

    top_p: Optional[float] = None

    stop: Optional[list[str]] = None


if TYPE_CHECKING:
    from .schema import ChatRequest


def build_generation_config(
    request: "ChatRequest",
) -> GenerationConfig:
    """
    根据 ChatRequest 创建生成参数配置。
    """

    return GenerationConfig(
        temperature=request.temperature,
        max_tokens=request.max_tokens,
    )


def generation_config_to_kwargs(
    config: GenerationConfig,
) -> dict:
    kwargs = {}

    if config.temperature is not None:
        kwargs["temperature"] = config.temperature

    if config.max_tokens is not None:
        kwargs["max_tokens"] = config.max_tokens

    if config.top_p is not None:
        kwargs["top_p"] = config.top_p

    if config.stop is not None:
        kwargs["stop"] = config.stop

    return kwargs
