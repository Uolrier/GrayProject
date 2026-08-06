from ..schema import RerankItem
from .schema import RankedDocument


class RerankAdapter:
    """
    Convert reranker result into ranking pipeline document.
    """

    @staticmethod
    def from_rerank_items(
        items: list[RerankItem],
    ) -> list[RankedDocument]:
        return [
            RankedDocument(
                id=item.id,
                content=item.text,
                rerank_score=item.score,
                final_score=item.score,
                metadata=item.metadata or {},
            )
            for item in items
        ]
