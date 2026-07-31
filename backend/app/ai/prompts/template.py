class PromptTemplate:
    """
    Prompt template renderer.

    Responsible for rendering prompt text
    with provided variables.
    """

    def __init__(
        self,
        template: str,
        variables: list[str] | None = None,
    ):
        self.template = template
        self.variables = variables or []

    def format(
        self,
        **kwargs,
    ) -> str:
        """
        Render prompt template.

        Raises:
            ValueError:
                When required variables are missing.
        """

        missing = [variable for variable in self.variables if variable not in kwargs]

        if missing:
            raise ValueError(f"Missing prompt variables: {missing}")

        return self.template.format(**kwargs)
