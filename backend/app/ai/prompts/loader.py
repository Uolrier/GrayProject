from pathlib import Path

from backend.app.ai.prompts.template import PromptTemplate


class PromptLoader:
    """
    Load prompt templates from files.
    """

    def __init__(
        self,
        prompt_dir: str | Path,
    ):
        self.prompt_dir = Path(prompt_dir)

    def load(
        self,
        name: str,
        variables: list[str] | None = None,
    ) -> PromptTemplate:
        """
        Load prompt template from text file.
        """

        path = self.prompt_dir / f"{name}.txt"

        if not path.exists():
            raise FileNotFoundError(f"Prompt file not found: {path}")

        content = path.read_text(
            encoding="utf-8",
        )

        return PromptTemplate(
            template=content,
            variables=variables,
        )
