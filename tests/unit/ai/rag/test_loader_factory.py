from app.ai.rag.ingestion.factory import LoaderFactory


def test_text_loader_registered():
    loaders = LoaderFactory.list_loaders()

    assert "text" in loaders


def test_create_text_loader():
    loader = LoaderFactory.create("text", path="test.txt")

    assert loader is not None
