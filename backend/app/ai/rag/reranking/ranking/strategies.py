from .schema import RankedDocument


class ScoreNormalizer:
    """
    Normalize scores into range [0, 1].
    """

    def normalize(
        self,
        scores: list[float],
    ) -> list[float]:
        if not scores:
            return []

        max_score = max(scores)
        min_score = min(scores)

        if max_score == min_score:
            return [1.0 for _ in scores]

        return [(score - min_score) / (max_score - min_score) for score in scores]


class WeightedScoreFusion:
    """
    Combine multiple ranking scores.
    """

    def __init__(
        self,
        first_weight: float = 0.7,
        second_weight: float = 0.3,
    ):
        self.first_weight = first_weight
        self.second_weight = second_weight

    def fuse(
        self,
        first_score: float,
        second_score: float,
    ) -> float:
        return self.first_weight * first_score + self.second_weight * second_score


class TopKSelector:
    """
    Select top-k documents according to final score.
    """

    def __init__(
        self,
        k: int = 5,
    ):
        self.k = k

    def rank(
        self,
        documents: list[RankedDocument],
    ) -> list[RankedDocument]:
        return sorted(
            documents,
            key=lambda item: item.final_score,
            reverse=True,
        )[: self.k]
