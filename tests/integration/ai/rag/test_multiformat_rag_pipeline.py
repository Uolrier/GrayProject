from backend.app.ai.rag.knowledgebase.manager import KnowledgeBaseManager
from backend.app.ai.rag.knowledgebase.persistence import (
    KnowledgeBasePersistence,
)
from backend.app.ai.rag.knowledgebase.schema import KnowledgeBaseConfig
from backend.app.ai.rag.runtime.manager import RAGRuntimeManager


def test_multiformat_rag_pipeline(tmp_path):
    """
    Multi format document RAG integration test.

    Flow:

    directory
        |
        v
    directory importer
        |
        v
    multiple loaders
        |
        v
    index pipeline
        |
        v
    vector store
        |
        v
    retrieval
        |
        v
    rag answer
    """

    # ------------------------
    # create mixed documents
    # ------------------------

    knowledge_dir = tmp_path / "knowledge"
    knowledge_dir.mkdir()

    files = {
        "README.md": """
# GrayProject

GrayProject is an AI assistant project.
It contains RAG pipeline.
""",
        "example.py": """
class KnowledgeManager:
    def load_document(self):
        return "python loader example"
""",
        "Example.java": """
public class Example {
    public String name(){
        return "java example";
    }
}
""",
        "index.js": """
function hello(){
    return "javascript example";
}
""",
        "config.json": """
{
    "project": "GrayProject",
    "feature": "RAG"
}
""",
        "sample.cpp": """
#include <iostream>

int main(){
    std::cout<<"cpp example";
}
""",
        "page.html": """
<html>
<body>
GrayProject html document
</body>
</html>
""",
        "note.txt": """
GrayProject text document.
""",
    }

    for filename, content in files.items():
        (knowledge_dir / filename).write_text(
            content,
            encoding="utf-8",
        )

    # ------------------------
    # create knowledge base
    # ------------------------

    config = KnowledgeBaseConfig(
        name="multiformat_test",
        type="local",
        embedding="dummy",
        vectordb="chroma",
    )

    manager = KnowledgeBaseManager(
        persistence=KnowledgeBasePersistence(path=tmp_path / "knowledge_bases.json")
    )

    kb = manager.create(config)

    result = kb.add(
        path=str(knowledge_dir),
    )

    # ------------------------
    # verify indexing
    # ------------------------

    assert result["documents"] >= len(files)

    assert result["chunks"] > 0

    # ------------------------
    # create rag service
    # ------------------------

    service = RAGRuntimeManager.create_chat_service(
        knowledge_base_manager=manager,
        knowledge_base_name="multiformat_test",
    )

    response = service.chat("GrayProject是什么项目?")

    # ------------------------
    # verify response
    # ------------------------

    assert response.answer

    assert "GrayProject" in response.answer

    assert len(response.sources) > 0
