from app.ai.rag.reranking.ranking.pipeline import RankingPipeline
from app.ai.rag.reranking.ranking.schema import RankedDocument
from app.ai.rag.reranking.ranking.strategies import (
    ScoreNormalizer,
    TopKSelector,
    WeightedScoreFusion,
)


def test_score_normalizer():
    normalizer = ScoreNormalizer()

    result = normalizer.normalize(
        [
            10,
            20,
            30,
        ]
    )

    assert result == [
        0.0,
        0.5,
        1.0,
    ]


def test_weighted_score_fusion():
    fusion = WeightedScoreFusion(
        first_weight=0.7,
        second_weight=0.3,
    )

    score = fusion.fuse(
        1.0,
        0.0,
    )

    assert score == 0.7


def test_top_k_selector():
    documents = [
        RankedDocument(
            id="1",
            content="doc1",
            final_score=0.3,
        ),
        RankedDocument(
            id="2",
            content="doc2",
            final_score=0.9,
        ),
        RankedDocument(
            id="3",
            content="doc3",
            final_score=0.5,
        ),
    ]

    selector = TopKSelector(
        k=2,
    )

    result = selector.rank(documents)

    assert len(result) == 2
    assert result[0].id == "2"
    assert result[1].id == "3"


def test_ranking_pipeline():
    documents = [
        RankedDocument(
            id="1",
            content="a",
            final_score=0.2,
        ),
        RankedDocument(
            id="2",
            content="b",
            final_score=0.8,
        ),
    ]

    pipeline = RankingPipeline(
        strategies=[
            TopKSelector(k=1),
        ]
    )

    result = pipeline.execute(documents)

    assert len(result) == 1
    assert result[0].id == "2"
