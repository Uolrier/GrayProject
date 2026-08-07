from fastapi import APIRouter

from backend.app.ai.rag.chat.schema import (
    RagChatRequest,
    RagChatResponse,
)
from backend.app.ai.rag.chat.service import (
    RagChatService,
)

router = APIRouter(
    prefix="/rag",
    tags=["RAG Chat"],
)


_service: RagChatService | None = None


def get_rag_chat_service():
    if _service is None:
        raise RuntimeError("RAG Chat service is not initialized")

    return _service


def register_rag_chat_service(
    service: RagChatService,
):
    global _service

    _service = service


@router.post(
    "/chat",
    response_model=RagChatResponse,
)
def rag_chat(
    request: RagChatRequest,
):
    service = get_rag_chat_service()

    return service.chat(
        request.query,
    )
