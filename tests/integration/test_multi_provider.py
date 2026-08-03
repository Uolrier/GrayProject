import pytest

from backend.app.llm.registry import get_provider


@pytest.mark.integration
def test_openai_provider_registered():
    provider = get_provider("openai")

    assert provider is not None
    assert provider.__name__ == "OpenAILLM"


@pytest.mark.integration
def test_deepseek_provider_registered():
    provider = get_provider("deepseek")

    assert provider is not None
    assert provider.__name__ == "DeepSeekLLM"
