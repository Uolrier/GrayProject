from .cross_encoder import CrossEncoderReranker


class BGEReranker(CrossEncoderReranker):
    """
    BGE Cross Encoder Reranker.
    """

    name = "bge"

    def __init__(
        self,
        model_name: str = "BAAI/bge-reranker-base",
        device: str | None = None,
    ):
        super().__init__(
            model_name=model_name,
            device=device,
        )
