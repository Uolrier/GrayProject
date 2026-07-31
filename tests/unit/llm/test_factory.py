from backend.app.llm.base import BaseLLM
from backend.app.llm.factory import LLMFactory
from backend.app.llm.registry import register_provider
from backend.app.llm.schema import ChatResponse


@register_provider("fake")
class FakeLLM(BaseLLM):
    model_name = "fake-model"

    def chat(self, request):
        return ChatResponse(content="mock response")

    def generate(self, prompt: str) -> str:
        return prompt

    def stream(self, prompt: str):
        yield prompt


def test_create_llm():
    llm = LLMFactory.create("fake")

    assert isinstance(llm, FakeLLM)
