from .pipeline import QueryPipeline


class QueryPipelineBuilder:
    def __init__(
        self,
        retriever,
        reranker=None,
        context_builder=None,
    ):
        self.retriever = retriever
        self.reranker = reranker
        self.context_builder = context_builder

    def build(self):
        return QueryPipeline(
            retriever=self.retriever,
            reranker=self.reranker,
            context_builder=self.context_builder,
        )
