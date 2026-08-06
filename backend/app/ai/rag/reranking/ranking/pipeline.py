from .base import RankingStrategy


class RankingPipeline:
    """
    Execute multiple ranking strategies sequentially.
    """

    def __init__(
        self,
        strategies: list[RankingStrategy] | None = None,
    ):
        self.strategies = strategies or []

    def add(
        self,
        strategy: RankingStrategy,
    ):
        """
        Add ranking strategy.
        """

        self.strategies.append(strategy)

    def execute(
        self,
        documents,
    ):
        """
        Run ranking pipeline.
        """

        result = documents

        for strategy in self.strategies:
            result = strategy.rank(result)

        return result
