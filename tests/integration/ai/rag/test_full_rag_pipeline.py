from backend.app.ai.rag.knowledgebase.manager import KnowledgeBaseManager
from backend.app.ai.rag.knowledgebase.persistence import (
    KnowledgeBasePersistence,
)
from backend.app.ai.rag.knowledgebase.schema import (
    KnowledgeBaseConfig,
)
from backend.app.ai.rag.runtime.manager import (
    RAGRuntimeManager,
)


def test_full_rag_pipeline(tmp_path):
    """
    Full RAG pipeline test.

    Flow:

    document
        |
        v
    loader
        |
        v
    index
        |
        v
    vector store
        |
        v
    retrieval
        |
        v
    llm answer
    """

    # ------------------------
    # create test document
    # ------------------------

    document = tmp_path / "grayproject.md"

    document.write_text(
        """
# GrayProject

GrayProject 是一个个人 AI 管理系统项目。

它使用 FastAPI 作为后端。

项目实现了 RAG Pipeline。

包括：

- 文档加载
- Embedding
- Chroma Vector Database
- Retriever
- Context Builder
""",
        encoding="utf-8",
    )

    # ------------------------
    # create knowledge base
    # ------------------------

    config = KnowledgeBaseConfig(
        name="test_grayproject",
        type="local",
        embedding="dummy",
        vectordb="chroma",
    )

    knowledge_base_manager = KnowledgeBaseManager(
        persistence=KnowledgeBasePersistence(path=tmp_path / "knowledge_bases.json")
    )

    kb = knowledge_base_manager.create(config)

    result = kb.add(
        path=str(document),
    )

    assert result["documents"] == 1

    assert result["chunks"] > 0

    # ------------------------
    # create rag service
    # ------------------------

    service = RAGRuntimeManager.create_chat_service(
        knowledge_base_manager=knowledge_base_manager,
        knowledge_base_name="test_grayproject",
    )

    response = service.chat("GrayProject是什么?")

    # ------------------------
    # verify answer
    # ------------------------

    assert response.answer

    assert "GrayProject" in response.answer

    assert len(response.sources) > 0
