from .schema import (
    RetrievalEvaluationCase,
    RetrievalEvaluationResult,
)


class RetrievalEvaluator:
    """
    Evaluate retriever accuracy.
    """

    def __init__(
        self,
        retriever,
    ):
        self.retriever = retriever

    def evaluate_case(
        self,
        case: RetrievalEvaluationCase,
        top_k: int = 5,
    ) -> RetrievalEvaluationResult:
        """
        Evaluate single query.
        """

        documents = self.retriever.search(
            query=case.query,
            top_k=top_k,
        )

        sources = []

        for doc in documents:
            source = None

            if doc.metadata:
                source = doc.metadata.get("source")

            if source:
                sources.append(source)

        hit = False
        first_hit_rank = None

        for index, source in enumerate(
            sources,
            start=1,
        ):
            if source in case.expected_sources:
                hit = True
                first_hit_rank = index
                break

        return RetrievalEvaluationResult(
            query=case.query,
            retrieved_sources=sources,
            hit=hit,
            first_hit_rank=first_hit_rank,
        )

    def evaluate(
        self,
        cases: list[RetrievalEvaluationCase],
        top_k: int = 5,
    ):
        """
        Evaluate multiple cases.
        """

        return [
            self.evaluate_case(
                case,
                top_k,
            )
            for case in cases
        ]
