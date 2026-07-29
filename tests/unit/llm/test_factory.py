import pytest

from backend.app.llm.base import BaseLLM
from backend.app.llm.factory import LLMFactory


class FakeLLM(BaseLLM):
    @property
    def model_name(self):
        return "fake"

    def generate(self, prompt: str):
        return f"response: {prompt}"

    def stream(self, prompt: str):
        yield prompt


def test_register_and_create_llm():
    LLMFactory.register("fake", FakeLLM)

    llm = LLMFactory.create("fake")

    assert isinstance(llm, FakeLLM)
    assert llm.model_name == "fake"


def test_create_unknown_provider():
    with pytest.raises(ValueError):
        LLMFactory.create("unknown")
