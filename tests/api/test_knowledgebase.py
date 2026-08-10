from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from backend.app.ai.rag.knowledgebase.manager import (
    KnowledgeBaseManager,
)
from backend.app.ai.rag.knowledgebase.persistence import (
    KnowledgeBasePersistence,
)
from backend.app.main import app
from backend.app.routers.knowledgebase import (
    register_knowledge_base_manager,
)
from backend.app.routers.rag_chat import (
    register_knowledge_base_manager as register_rag_manager,
)


@pytest.fixture(scope="module")
def client(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp("knowledgebase_test")
    manager = KnowledgeBaseManager(
        persistence=KnowledgeBasePersistence(path=tmp_path / "knowledge_bases.json")
    )
    register_knowledge_base_manager(manager)
    register_rag_manager(manager)
    return TestClient(app)


def test_create_knowledge_base(client):
    mock_embedding = MagicMock()
    mock_vector_store = MagicMock()

    with (
        patch(
            "backend.app.ai.rag.knowledgebase.providers.local.EmbeddingFactory.create",
            return_value=mock_embedding,
        ),
        patch(
            "backend.app.ai.rag.knowledgebase.providers.local.VectorStoreFactory.create",
            return_value=mock_vector_store,
        ),
    ):
        response = client.post(
            "/knowledge-bases",
            json={
                "name": "test_api_kb",
                "type": "local",
                "embedding": "bge",
                "vectordb": "chroma",
                "root_path": None,
                "auto_update": False,
                "watch_interval": 30,
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "test_api_kb"
    assert data["type"] == "local"
    assert data["status"] == "created"


def test_list_knowledge_bases(client):
    response = client.get("/knowledge-bases")

    assert response.status_code == 200

    data = response.json()

    assert "knowledge_bases" in data
    assert "test_api_kb" in data["knowledge_bases"]


def test_get_knowledge_base(client):
    response = client.get("/knowledge-bases/test_api_kb")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "test_api_kb"
    assert data["type"] == "local"
    assert data["embedding"] == "bge"
    assert data["vectordb"] == "chroma"


def test_get_missing_knowledge_base(client):
    response = client.get("/knowledge-bases/not_exists")

    assert response.status_code == 404


def test_delete_knowledge_base(client):
    response = client.delete("/knowledge-bases/test_api_kb")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "test_api_kb"
    assert data["status"] == "deleted"


def test_delete_missing_knowledge_base(client):
    response = client.delete("/knowledge-bases/not_exists")

    assert response.status_code == 404
