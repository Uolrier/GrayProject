from abc import ABC, abstractmethod

from .schema import QueryRequest, QueryResponse


class BaseQueryPipeline(ABC):
    @abstractmethod
    def run(
        self,
        request: QueryRequest,
    ) -> QueryResponse:
        pass
