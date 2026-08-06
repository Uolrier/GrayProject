from sentence_transformers import CrossEncoder

from ..base import BaseReranker
from ..schema import (
    RerankItem,
    RerankRequest,
    RerankResult,
)


class BGEReranker(BaseReranker):
    """
    BGE Cross Encoder Reranker.
    """

    name = "bge"

    def __init__(
        self,
        model_name: str = "BAAI/bge-reranker-base",
        device: str | None = None,
    ):
        self.model = CrossEncoder(
            model_name,
            device=device,
        )

    def rerank(
        self,
        request: RerankRequest,
    ) -> RerankResult:
        pairs = [
            (
                request.query,
                document.text,
            )
            for document in request.documents
        ]

        scores = self.model.predict(pairs)

        items = []

        for document, score in zip(
            request.documents,
            scores,
        ):
            items.append(
                RerankItem(
                    id=document.id,
                    score=float(score),
                    text=document.text,
                    metadata=document.metadata,
                )
            )

        items.sort(
            key=lambda item: item.score,
            reverse=True,
        )

        items = items[: request.top_k]

        return RerankResult(items=items)
