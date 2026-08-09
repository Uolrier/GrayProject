from typing import List


def hit_rate(
    results: List[bool],
) -> float:
    """
    Calculate hit rate.

    hit_rate =
        successful queries / total queries
    """

    if not results:
        return 0.0

    return sum(results) / len(results)


def precision_at_k(
    retrieved: List[str],
    expected: List[str],
    k: int,
) -> float:
    """
    Calculate Precision@K.
    """

    if k <= 0:
        return 0.0

    retrieved = retrieved[:k]

    if not retrieved:
        return 0.0

    hits = len(set(retrieved) & set(expected))

    return hits / len(retrieved)


def reciprocal_rank(
    rank: int | None,
) -> float:
    """
    Calculate reciprocal rank.
    """

    if rank is None:
        return 0.0

    if rank <= 0:
        return 0.0

    return 1 / rank


def mean_reciprocal_rank(
    ranks: List[int | None],
) -> float:
    """
    Calculate MRR.
    """

    if not ranks:
        return 0.0

    scores = [reciprocal_rank(rank) for rank in ranks]

    return sum(scores) / len(scores)
