from backend.app.llm.generation_config import (
    GenerationConfig,
    generation_config_to_kwargs,
)


def test_max_tokens_default():
    config = GenerationConfig()

    assert config.max_tokens is None


def test_max_tokens_custom():
    config = GenerationConfig(
        max_tokens=2048,
    )

    assert config.max_tokens == 2048


def test_max_tokens_to_kwargs():
    config = GenerationConfig(
        max_tokens=1024,
    )

    kwargs = generation_config_to_kwargs(config)

    assert kwargs["max_tokens"] == 1024
