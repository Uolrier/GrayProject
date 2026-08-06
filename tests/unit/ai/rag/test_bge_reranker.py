from unittest.mock import MagicMock, patch

from backend.app.ai.rag.reranking.providers.bge import BGEReranker
from backend.app.ai.rag.reranking.schema import (
    RerankDocument,
    RerankRequest,
)


def test_bge_reranker():
    with patch("app.ai.rag.reranking.providers.cross_encoder.CrossEncoder") as mock:
        model = MagicMock()

        model.predict.return_value = [
            0.2,
            0.9,
        ]

        mock.return_value = model

        reranker = BGEReranker()

        request = RerankRequest(
            query="python",
            documents=[
                RerankDocument(
                    id="1",
                    text="python code",
                ),
                RerankDocument(
                    id="2",
                    text="cat",
                ),
            ],
            top_k=2,
        )

        result = reranker.rerank(request)

        assert len(result.items) == 2

        # score 高的排前面
        assert result.items[0].id == "2"
        assert result.items[0].score == 0.9


def test_bge_reranker_top_k():
    with patch("app.ai.rag.reranking.providers.cross_encoder.CrossEncoder") as mock:
        model = MagicMock()

        model.predict.return_value = [
            0.8,
            0.5,
            0.1,
        ]

        mock.return_value = model

        reranker = BGEReranker()

        request = RerankRequest(
            query="test",
            documents=[
                RerankDocument(
                    id="1",
                    text="a",
                ),
                RerankDocument(
                    id="2",
                    text="b",
                ),
                RerankDocument(
                    id="3",
                    text="c",
                ),
            ],
            top_k=2,
        )

        result = reranker.rerank(request)

        assert len(result.items) == 2
        assert result.items[0].score == 0.8
        assert result.items[1].score == 0.5
