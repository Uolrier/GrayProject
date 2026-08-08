import uuid

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.app.ai.rag.chat.schema import (
    RagChatRequest,
    RagChatResponse,
)
from backend.app.ai.rag.chat.service import (
    RagChatService,
)
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


@router.post("/chat/stop")
async def stop_rag_generation(request):
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
    service = get_rag_chat_service()

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
