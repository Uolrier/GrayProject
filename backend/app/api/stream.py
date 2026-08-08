"""
SSE encoder for LLM streaming chunks.
"""

from __future__ import annotations

import json

from backend.app.llm.stream import StreamChunk


def encode_chunk(chunk: StreamChunk) -> str:
    """
    Convert StreamChunk into SSE message.
    """

    payload = {
        "content": chunk.content,
        "finished": chunk.finished,
        "finish_reason": chunk.finish_reason,
    }

    return (
        "event: message\n"
        "data: "
        + json.dumps(
            payload,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        + "\n\n"
    )


def encode_done() -> str:
    """
    End of SSE stream.
    """

    return "data: [DONE]\n\n"


def encode_error(
    message: str,
    code: str = "INTERNAL_ERROR",
) -> str:
    """
    Encode SSE error event.

    Args:
        message:
            Error message.

        code:
            Error code.
    """

    payload = {
        "code": code,
        "message": message,
    }

    return (
        "event: error\n"
        "data: "
        + json.dumps(
            payload,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        + "\n\n"
    )


def encode_init(task_id: str) -> str:
    """
    Encode SSE initialization event.
    """

    payload = {
        "task_id": task_id,
    }

    return (
        "event: init\n"
        "data: "
        + json.dumps(
            payload,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        + "\n\n"
    )
