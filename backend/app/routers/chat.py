import uuid

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from backend.app.api.stream import (
    encode_chunk,
    encode_done,
    encode_error,
    encode_init,
)
from backend.app.llm.factory import ModelManager
from backend.app.llm.generation import generation_manager

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/stop")
async def stop_generation(request: Request):
    """
    停止当前生成任务。
    """
    body = await request.json()

    task_id = body.get("task_id")

    if not task_id:
        return {"error": "task_id is required"}

    success = generation_manager.cancel(task_id)

    return {
        "success": success,
    }


@router.post("/stream")
async def chat_stream(request: Request):
    body = await request.json()

    prompt = body.get("message")

    if not prompt:
        return {"error": "message is required"}

    task_id = str(uuid.uuid4())
    generation_manager.create(task_id)

    llm = ModelManager.create_active()

    def generator():
        try:
            yield encode_init(task_id)

            for chunk in llm.stream(prompt):
                if generation_manager.is_cancelled(task_id):
                    break

                yield encode_chunk(chunk)

            yield encode_done()

        except Exception as exc:
            yield encode_error(str(exc))

        finally:
            generation_manager.remove(task_id)

    return StreamingResponse(
        generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
