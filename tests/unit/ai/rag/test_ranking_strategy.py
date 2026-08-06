from app.ai.rag.reranking.ranking.pipeline import RankingPipeline
from app.ai.rag.reranking.ranking.strategies import (
    ScoreNormalizer,
    TopKSelector,
    WeightedScoreFusion,
)


def test_score_normalizer_empty():
    normalizer = ScoreNormalizer()

    result = normalizer.normalize([])

    assert result == []


def test_score_normalizer_same_scores():
    normalizer = ScoreNormalizer()

    result = normalizer.normalize(
        [
            1.0,
            1.0,
            1.0,
        ]
    )

    assert result == [
        1.0,
        1.0,
        1.0,
    ]


def test_weighted_fusion_custom_weight():
    fusion = WeightedScoreFusion(
        first_weight=0.5,
        second_weight=0.5,
    )

    result = fusion.fuse(
        0.8,
        0.2,
    )

    assert result == 0.5


def test_pipeline_add_strategy():
    pipeline = RankingPipeline()

    pipeline.add(
        TopKSelector(
            k=1,
        )
    )

    assert len(pipeline.strategies) == 1
