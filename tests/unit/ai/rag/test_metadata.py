from app.ai.rag.metadata import Metadata, MetadataManager


def test_metadata_create():
    metadata = Metadata(document_id="doc1", source="test.md", file_type="markdown")

    assert metadata.document_id == "doc1"

    data = metadata.to_dict()

    assert data["source"] == "test.md"


def test_metadata_manager():
    manager = MetadataManager()

    metadata = Metadata(document_id="doc1")

    manager.add(metadata)

    result = manager.get("doc1")

    assert result is not None


def test_metadata_update():
    manager = MetadataManager()

    manager.add(Metadata(document_id="doc1"))

    manager.update("doc1", source="README.md")

    result = manager.get("doc1")

    assert result.source == "README.md"
