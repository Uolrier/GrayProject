from backend.app.llm.generation_config import (
    GenerationConfig,
    generation_config_to_kwargs,
)


def test_top_p_default():
    config = GenerationConfig()

    assert config.top_p is None


def test_top_p_to_kwargs():
    config = GenerationConfig(top_p=0.9)

    kwargs = generation_config_to_kwargs(config)

    assert kwargs["top_p"] == 0.9
