from .schema import QueryRequest


class QueryService:
    def __init__(
        self,
        pipeline,
    ):
        self.pipeline = pipeline

    def query(
        self,
        text: str,
    ):
        request = QueryRequest(
            query=text,
        )

        return self.pipeline.run(
            request,
        )
