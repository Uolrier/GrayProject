from .registry import RuntimeRegistry


class RuntimeFactory:
    """
    Factory for creating local inference runtimes.
    """

    @staticmethod
    def create(
        name: str,
        **kwargs,
    ):
        """
        Create runtime instance.

        Args:
            name:
                Runtime name registered in RuntimeRegistry.

            kwargs:
                Runtime initialization parameters.
        """

        runtime_cls = RuntimeRegistry.get(name)

        return runtime_cls(**kwargs)
