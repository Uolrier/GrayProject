from pathlib import Path

from backend.app.ai.prompts.loader import PromptLoader
from backend.app.ai.prompts.template import PromptTemplate


class PromptManager:
    """
    Prompt template registry and manager.
    """

    def __init__(self):
        self._templates: dict[str, PromptTemplate] = {}

    def register(
        self,
        name: str,
        template: PromptTemplate,
    ) -> None:
        """
        Register a prompt template.
        """

        self._templates[name] = template

    def get(
        self,
        name: str,
    ) -> PromptTemplate:
        """
        Get a prompt template.
        """

        if name not in self._templates:
            raise KeyError(f"Prompt template not found: {name}")

        return self._templates[name]

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._templates

    def list_templates(self) -> list[str]:
        return list(self._templates.keys())

    def load_builtin(
        self,
        prompt_dir: str | Path,
        variables: dict[str, list[str]] | None = None,
    ) -> None:
        """
        Load builtin prompt templates.
        """

        loader = PromptLoader(prompt_dir)

        for file in Path(prompt_dir).glob("*.txt"):
            name = file.stem

            template = loader.load(
                name=name,
                variables=(variables.get(name) if variables else None),
            )

            self.register(
                name,
                template,
            )
