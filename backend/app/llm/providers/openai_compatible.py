"""
OpenAI Compatible LLM base implementation.

Provide common logic for all providers exposing an
OpenAI-compatible API.
"""

# from typing import Iterator
from collections.abc import Generator

from openai import APITimeoutError, OpenAI

from ...core.exceptions import LLMTimeoutError
from ...core.retry import retry
from ...core.timeout import (
    get_retry_config,
    get_timeout_config,
)
from ..base import BaseLLM
from ..generation_config import (
    build_generation_config,
    generation_config_to_kwargs,
)
from ..schema import ChatRequest, ChatResponse, TokenUsage
from ..stream import StreamChunk


class OpenAICompatibleLLM(BaseLLM):
    """
    OpenAI Compatible Provider Base Class

    所有兼容 OpenAI API 的 Provider
    都应继承该类。
    """

    def __init__(
        self,
        *,
        api_key: str,
        model_name: str,
        base_url: str | None = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self._model_name = model_name

        self.client = None

    def _get_client(self) -> OpenAI:
        """
        Lazy initialize OpenAI client.
        """

        if self.client is None:
            timeout_config = get_timeout_config()

            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
                timeout=timeout_config.total,
            )

        return self.client

    @property
    def model_name(self) -> str:
        return self._model_name

    def chat(self, request: ChatRequest) -> ChatResponse:
        """
        Chat completion interface.
        """

        client = self._get_client()

        messages = []

        if request.system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": request.system_prompt,
                }
            )

        messages.extend(
            [
                {
                    "role": msg.role,
                    "content": msg.content,
                }
                for msg in request.messages
            ]
        )

        generation_config = build_generation_config(request)

        generation_kwargs = generation_config_to_kwargs(generation_config)

        retry_config = get_retry_config()

        @retry(
            max_attempts=retry_config.max_attempts,
            backoff_factor=retry_config.backoff_factor,
        )
        def create_completion():
            return client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                stream=False,
                **generation_kwargs,
            )

        try:
            response = create_completion()

        except APITimeoutError as exc:
            raise LLMTimeoutError() from exc

        usage = None

        if response.usage:
            usage = TokenUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            )

        return ChatResponse(
            content=response.choices[0].message.content,
            model=response.model,
            provider=self.__class__.__name__,
            usage=usage,
        )

    def generate(self, prompt: str, **kwargs) -> str:
        client = self._get_client()

        retry_config = get_retry_config()

        @retry(
            max_attempts=retry_config.max_attempts,
            backoff_factor=retry_config.backoff_factor,
        )
        def create_completion():
            return client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                **kwargs,
            )

        try:
            response = create_completion()

        except APITimeoutError as exc:
            raise LLMTimeoutError() from exc

        return response.choices[0].message.content

    def stream(
        self,
        prompt: str | None = None,
        messages=None,
        **kwargs,
    ) -> Generator[StreamChunk, None, None]:
        client = self._get_client()

        if messages is None:
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                }
            ]

        else:
            messages = [
                {
                    "role": msg.role,
                    "content": msg.content,
                }
                for msg in messages
            ]

        response = client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            stream=True,
            **kwargs,
        )

        for chunk in response:
            choice = chunk.choices[0]
            content = choice.delta.content or ""

            if content:
                yield StreamChunk(
                    content=content,
                )

            if choice.finish_reason is not None:
                yield StreamChunk(
                    content="",
                    finished=True,
                    finish_reason=choice.finish_reason,
                )
