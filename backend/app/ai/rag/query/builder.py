from .pipeline import QueryPipeline


class QueryPipelineBuilder:
    def __init__(
        self,
        retriever,
        reranker=None,
    ):
        self.retriever = retriever
        self.reranker = reranker

    def build(self):
        return QueryPipeline(
            retriever=self.retriever,
            reranker=self.reranker,
        )
