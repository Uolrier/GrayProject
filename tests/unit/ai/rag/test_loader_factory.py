from app.ai.rag.ingestion.factory import LoaderFactory
from app.ai.rag.ingestion.loaders.python import PythonLoader


def test_text_loader_registered():
    loaders = LoaderFactory.list_loaders()

    assert "text" in loaders


def test_create_text_loader():
    loader = LoaderFactory.create("text", path="test.txt")

    assert loader is not None


def test_python_loader_registered():
    loaders = LoaderFactory.list_loaders()

    assert "python" in loaders


def test_create_python_loader():
    loader = LoaderFactory.create(
        "python",
        path="demo.py",
    )

    assert isinstance(
        loader,
        PythonLoader,
    )
