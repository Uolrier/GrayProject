from app.ai.rag.reranking.ranking.adapter import RerankAdapter
from app.ai.rag.reranking.schema import RerankItem


def test_rerank_adapter():
    items = [
        RerankItem(
            id="1",
            score=0.9,
            text="hello",
        )
    ]

    result = RerankAdapter.from_rerank_items(items)

    assert result[0].id == "1"
    assert result[0].rerank_score == 0.9
    assert result[0].final_score == 0.9
