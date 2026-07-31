import pytest

from backend.app.llm.base import BaseLLM
from backend.app.llm.schema import ChatResponse


class MockLLM(BaseLLM):
    @property
    def model_name(self):
        return "mock-model"

    def chat(self, request):
        return ChatResponse(content="mock response")

    def generate(self, prompt, **kwargs):
        return f"response: {prompt}"

    def stream(self, prompt, **kwargs):
        yield f"response: {prompt}"


def test_base_llm_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseLLM()


def test_mock_llm_generate():
    llm = MockLLM()

    result = llm.generate("hello")

    assert result == "response: hello"


def test_mock_llm_stream():
    llm = MockLLM()

    result = list(llm.stream("hello"))

    assert result == ["response: hello"]


def test_model_name():
    llm = MockLLM()

    assert llm.model_name == "mock-model"
