from backend.app.ai.rag.ingestion import Document


def test_document_creation():
    doc = Document(page_content="hello rag", metadata={"source": "test.txt"})

    assert doc.page_content == "hello rag"

    assert doc.metadata["source"] == "test.txt"
