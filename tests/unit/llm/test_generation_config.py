from backend.app.llm.generation_config import (
    GenerationConfig,
    build_generation_config,
)
from backend.app.llm.schema import ChatRequest


def test_default_generation_config():
    config = GenerationConfig()

    assert config.temperature == 0.7
    assert config.max_tokens == 2048


def test_custom_temperature():
    config = GenerationConfig(temperature=1.2)

    assert config.temperature == 1.2


def test_build_generation_config():
    request = ChatRequest(
        temperature=0.3,
        max_tokens=512,
    )

    config = build_generation_config(request)

    assert config.temperature == 0.3
    assert config.max_tokens == 512
