import uuid

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from backend.app.api.stream import (
    encode_chunk,
    encode_done,
    encode_error,
    encode_init,
)
from backend.app.core.exceptions import GrayException
from backend.app.llm.factory import ModelManager
from backend.app.llm.generation import generation_manager
from backend.app.llm.memory import (
    conversation_memory,
)
from backend.app.llm.schema import (
    ChatMessage,
)

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

    session_id = body.get(
        "session_id",
        "default",
    )

    if not prompt:
        return {"error": "message is required"}

    task_id = str(uuid.uuid4())
    generation_manager.create(task_id)

    def generator():
        try:
            conversation_memory.add_message(
                session_id,
                ChatMessage(
                    role="user",
                    content=prompt,
                ),
            )

            llm = ModelManager.create_active()

            yield encode_init(task_id)

            history = conversation_memory.get_history(session_id)

            answer = ""

            for chunk in llm.stream(
                messages=history,
            ):
                if generation_manager.is_cancelled(task_id):
                    break

                answer += chunk.content

                yield encode_chunk(chunk)

            conversation_memory.add_message(
                session_id,
                ChatMessage(
                    role="assistant",
                    content=answer,
                ),
            )

            yield encode_done()

        except GrayException as exc:
            yield encode_error(
                exc.message,
                exc.code,
            )

        except Exception:
            yield encode_error(
                "Internal server error",
                "INTERNAL_ERROR",
            )

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
