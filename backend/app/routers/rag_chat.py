import uuid

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse

from backend.app.ai.rag.chat.schema import (
    RagChatRequest,
    RagChatResponse,
)
from backend.app.ai.rag.chat.service import RagChatService
from backend.app.ai.rag.knowledgebase.manager import KnowledgeBaseManager
from backend.app.ai.rag.runtime.manager import RAGRuntimeManager
from backend.app.api.stream import (
    encode_chunk,
    encode_done,
    encode_init,
)
from backend.app.llm.generation import generation_manager

router = APIRouter(
    prefix="/rag",
    tags=["RAG Chat"],
)

_knowledge_base_manager: KnowledgeBaseManager | None = None


def register_knowledge_base_manager(
    manager: KnowledgeBaseManager,
):
    global _knowledge_base_manager

    _knowledge_base_manager = manager


def get_knowledge_base_manager() -> KnowledgeBaseManager:
    if _knowledge_base_manager is None:
        raise RuntimeError("Knowledge base manager is not initialized")

    return _knowledge_base_manager


def get_rag_chat_service(
    knowledge_base_name: str,
) -> RagChatService:
    manager = get_knowledge_base_manager()

    try:
        return RAGRuntimeManager.create_chat_service(
            knowledge_base_manager=manager,
            knowledge_base_name=knowledge_base_name,
        )
    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.post(
    "/chat",
    response_model=RagChatResponse,
)
def rag_chat(
    request: RagChatRequest,
):
    if not request.collection:
        raise HTTPException(
            status_code=400,
            detail="collection is required",
        )

    service = get_rag_chat_service(
        request.collection,
    )

    return service.chat(
        request.query,
    )


@router.post("/chat/stop")
async def stop_rag_generation(
    request: Request,
):
    body = await request.json()

    task_id = body.get("task_id")
    if not task_id:
        return {"error": "task_id is required"}
    success = generation_manager.cancel(task_id)
    return {
        "success": success,
    }


@router.post("/chat/stream")
def rag_chat_stream(
    request: RagChatRequest,
):
    if not request.collection:
        raise HTTPException(
            status_code=400,
            detail="collection is required",
        )

    service = get_rag_chat_service(
        request.collection,
    )

    task_id = str(uuid.uuid4())

    generation_manager.create(task_id)

    def event_generator():
        try:
            yield encode_init(task_id)

            for chunk in service.stream_chat(request.query):
                if generation_manager.is_cancelled(task_id):
                    break

                yield encode_chunk(chunk)

            yield encode_done()

        finally:
            generation_manager.remove(task_id)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
