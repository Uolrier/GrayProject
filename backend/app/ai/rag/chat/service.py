from backend.app.ai.rag.chat.schema import RagChatResponse
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

        return RagChatResponse(
            answer=answer,
            sources=response.sources or [],
        )

    def _build_prompt(
        self,
        query: str,
        context: str | None,
    ) -> str:
        if context is None:
            context = ""

        return f"""
You are a helpful AI assistant.

Instructions:
- Use the provided context when it is relevant.
- If the context does not contain useful information,
answer using your general knowledge.
- Do not mention the context unless necessary.
- Provide a clear and helpful answer.


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
