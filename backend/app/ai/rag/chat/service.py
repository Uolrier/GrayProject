from backend.app.llm.factory import ModelManager
from backend.app.llm.schema import ChatMessage


class RagChatService:
    """
    RAG Chat Service

    Flow:

    User Query
        |
        v
    QueryService
        |
        v
    QueryPipeline
        |
        v
    Context
        |
        v
    LLM
    """

    def __init__(
        self,
        query_service,
        llm=None,
    ):
        self.query_service = query_service

        self.llm = llm if llm is not None else ModelManager.create_active()

    def chat(
        self,
        query: str,
    ):
        response = self.query_service.query(
            query,
        )

        prompt = self._build_prompt(
            query,
            response.context,
        )

        answer = self.llm.generate(
            prompt,
        )

        return {
            "answer": answer,
            "sources": response.sources or [],
        }

    def _build_prompt(
        self,
        query: str,
        context: str | None,
    ):
        if context is None:
            context = ""

        return f"""
You are a helpful AI assistant.

Answer the question using the provided context.

Context:
{context}


Question:
{query}
"""

    def stream_chat(
        self,
        query: str,
    ):
        response = self.query_service.query(query)

        prompt = self._build_prompt(
            query,
            response.context,
        )

        messages = [
            ChatMessage(
                role="user",
                content=prompt,
            )
        ]

        for chunk in self.llm.stream(
            messages=messages,
        ):
            yield chunk
