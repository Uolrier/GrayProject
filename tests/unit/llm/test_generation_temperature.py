from backend.app.llm.generation_config import (
    build_generation_config,
    generation_config_to_kwargs,
)
from backend.app.llm.schema import ChatRequest


def test_temperature_mapping():
    request = ChatRequest(
        temperature=0.2,
        max_tokens=512,
    )

    config = build_generation_config(request)

    kwargs = generation_config_to_kwargs(config)

    assert kwargs["temperature"] == 0.2
    assert kwargs["max_tokens"] == 512
