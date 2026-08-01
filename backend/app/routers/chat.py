from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from backend.app.api.stream import (
    encode_chunk,
    encode_done,
    encode_error,
)
from backend.app.llm.factory import ModelManager

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/stream")
async def chat_stream(request: Request):
    body = await request.json()

    prompt = body.get("message")

    if not prompt:
        return {"error": "message is required"}

    llm = ModelManager.create_active()

    def generator():
        try:
            for chunk in llm.stream(prompt):
                yield encode_chunk(chunk)

            yield encode_done()

        except Exception as exc:
            yield encode_error(str(exc))

    return StreamingResponse(
        generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
