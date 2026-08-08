from dataclasses import dataclass

from fastapi import APIRouter, HTTPException

from backend.app.ai.rag.knowledgebase.manager import KnowledgeBaseManager
from backend.app.ai.rag.knowledgebase.schema import KnowledgeBaseConfig

router = APIRouter(
    prefix="/knowledge-bases",
    tags=["Knowledge Base"],
)

_knowledge_base_manager: KnowledgeBaseManager | None = None


@dataclass
class KnowledgeBaseDocumentRequest:
    path: str


def register_knowledge_base_manager(
    manager: KnowledgeBaseManager,
):
    global _knowledge_base_manager

    _knowledge_base_manager = manager


def get_knowledge_base_manager() -> KnowledgeBaseManager:
    if _knowledge_base_manager is None:
        raise RuntimeError("Knowledge base manager is not initialized")

    return _knowledge_base_manager


@router.post("")
def create_knowledge_base(
    config: KnowledgeBaseConfig,
):
    manager = get_knowledge_base_manager()

    try:
        manager.create(config)

    except ValueError as exc:
        raise HTTPException(
            status_code=409,
            detail=str(exc),
        ) from exc

    return {
        "name": config.name,
        "type": config.type,
        "root_path": config.root_path,
        "auto_update": config.auto_update,
        "status": "created",
    }


@router.get("")
def list_knowledge_bases():
    manager = get_knowledge_base_manager()

    return {
        "knowledge_bases": manager.list(),
    }


@router.get("/{name}")
def get_knowledge_base(
    name: str,
):
    manager = get_knowledge_base_manager()

    try:
        knowledge_base = manager.get(name)

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    config = knowledge_base.config

    return {
        "name": config.name,
        "type": config.type,
        "embedding": config.embedding,
        "vectordb": config.vectordb,
        "reranker": config.reranker,
        "root_path": config.root_path,
        "auto_update": config.auto_update,
        "watch_interval": config.watch_interval,
    }


@router.post("/{name}/documents")
def add_documents(
    name: str,
    request: KnowledgeBaseDocumentRequest,
):
    manager = get_knowledge_base_manager()

    try:
        knowledge_base = manager.get(name)

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    try:
        result = knowledge_base.add(request.path)

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail=f"Path not found: {request.path}",
        ) from exc

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    return {
        "name": name,
        "path": request.path,
        "status": "indexed",
        "result": result,
    }


@router.delete("/{name}")
def delete_knowledge_base(
    name: str,
):
    manager = get_knowledge_base_manager()

    try:
        manager.delete(name)

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    return {
        "name": name,
        "status": "deleted",
    }
