from pathlib import Path

from backend.app.ai.prompts import PromptManager


def test_builtin_prompt_loading():
    manager = PromptManager()

    manager.load_builtin(
        Path("backend/app/ai/prompts/builtin"),
        variables={
            "chat": [
                "input",
            ],
        },
    )

    assert manager.exists(
        "chat",
    )

    prompt = manager.get(
        "chat",
    )

    result = prompt.format(
        input="Hello GrayProject",
    )

    assert "Hello GrayProject" in result
