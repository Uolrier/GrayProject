from unittest.mock import patch

from fastapi.testclient import TestClient

from backend.app.llm.stream import StreamChunk
from backend.app.main import app

client = TestClient(app)


class MockLLM:
    def stream(
        self,
        prompt=None,
        messages=None,
        **kwargs,
    ):
        yield StreamChunk(content="Hello")

        yield StreamChunk(
            content=" World",
        )

        yield StreamChunk(
            content="",
            finished=True,
            finish_reason="stop",
        )


def test_chat_stream_sse():
    """
    Test SSE streaming response.
    """

    with patch(
        "backend.app.routers.chat.ModelManager.create_active",
        return_value=MockLLM(),
    ):
        response = client.post(
            "/chat/stream",
            json={
                "message": "hello",
            },
        )

    assert response.status_code == 200

    assert response.headers["content-type"].startswith("text/event-stream")

    body = response.text

    assert 'data: {"content":"Hello"' in body

    assert 'data: {"content":" World"' in body

    assert '"finish_reason":"stop"' in body

    assert "data: [DONE]" in body
