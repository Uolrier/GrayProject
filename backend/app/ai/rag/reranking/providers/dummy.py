from ..base import BaseReranker
from ..schema import (
    RerankItem,
    RerankResult,
)


class DummyReranker(BaseReranker):
    name = "dummy"

    def rerank(self, request):
        items = []

        for index, doc in enumerate(request.documents):
            items.append(
                RerankItem(
                    id=doc.id,
                    score=1.0 - index * 0.1,
                    text=doc.text,
                    metadata=doc.metadata,
                )
            )

        return RerankResult(items=items[: request.top_k])
