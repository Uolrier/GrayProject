from unittest.mock import MagicMock, patch

from backend.app.ai.rag.reranking.providers.cross_encoder import (
    CrossEncoderReranker,
)
from backend.app.ai.rag.reranking.schema import (
    RerankDocument,
    RerankRequest,
)


def test_cross_encoder_reranker():
    with patch(
        "backend.app.ai.rag.reranking.providers.cross_encoder.CrossEncoder"
    ) as mock:
        model = MagicMock()

        model.predict.return_value = [
            0.1,
            0.9,
        ]

        mock.return_value = model

        reranker = CrossEncoderReranker("fake-model")

        mock.assert_called_once()

        result = reranker.rerank(
            RerankRequest(
                query="hello",
                documents=[
                    RerankDocument(
                        id="1",
                        text="bad",
                    ),
                    RerankDocument(
                        id="2",
                        text="good",
                    ),
                ],
                top_k=1,
            )
        )

        assert len(result.items) == 1

        assert result.items[0].id == "2"

        assert result.items[0].score == 0.9
