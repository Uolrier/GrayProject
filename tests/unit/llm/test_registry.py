from backend.app.llm.base import BaseLLM
from backend.app.llm.factory import LLMFactory
from backend.app.llm.registry import register_provider


@register_provider("test")
class TestLLM(BaseLLM):
    model_name = "test-model"

    def generate(self, prompt: str) -> str:
        return prompt

    def stream(self, prompt: str):
        yield prompt


def test_provider_registration():
    llm = LLMFactory.create("test")

    assert isinstance(llm, TestLLM)
