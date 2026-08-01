from collections.abc import Generator

from backend.app.llm.base import BaseLLM
from backend.app.llm.schema import ChatRequest, ChatResponse
from backend.app.llm.stream import StreamChunk


def test_stream_chunk_default():
    chunk = StreamChunk(content="Hello")

    assert chunk.content == "Hello"
    assert chunk.finished is False
    assert chunk.finish_reason is None


def test_stream_chunk_finished():
    chunk = StreamChunk(
        content="",
        finished=True,
        finish_reason="stop",
    )

    assert chunk.finished is True
    assert chunk.finish_reason == "stop"


class DummyLLM(BaseLLM):
    @property
    def model_name(self):
        return "dummy"

    def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        raise NotImplementedError

    def generate(self, prompt, **kwargs):
        return "Hello"

    def stream(
        self,
        prompt: str,
        **kwargs,
    ) -> Generator[StreamChunk, None, None]:
        yield StreamChunk("Hel")
        yield StreamChunk("lo")
        yield StreamChunk(
            "",
            finished=True,
            finish_reason="stop",
        )


def test_stream_collect():
    llm = DummyLLM()

    chunks = list(llm.stream("Hello"))

    assert len(chunks) == 3

    text = "".join(c.content for c in chunks)

    assert text == "Hello"


def test_last_chunk_finished():
    llm = DummyLLM()

    chunks = list(llm.stream("test"))

    assert chunks[-1].finished is True
    assert chunks[-1].finish_reason == "stop"
