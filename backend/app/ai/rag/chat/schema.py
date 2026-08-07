from pydantic import BaseModel, Field


class RagChatRequest(BaseModel):
    """
    RAG Chat request
    """

    query: str = Field(
        ...,
        min_length=1,
        description="User question",
    )

    collection: str | None = Field(
        default=None,
        description="Knowledge collection",
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Retrieval top k",
    )

    session_id: str | None = Field(
        default=None,
        description="Conversation session id",
    )


class RagChatResponse(BaseModel):
    """
    RAG Chat response
    """

    answer: str

    sources: list[str] = []
