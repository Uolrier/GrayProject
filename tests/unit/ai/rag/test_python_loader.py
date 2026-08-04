from backend.app.ai.rag.ingestion.loaders.python import PythonLoader


def test_python_loader(tmp_path):
    file = tmp_path / "demo.py"

    file.write_text("print('hello')", encoding="utf-8")

    loader = PythonLoader()

    docs = loader.load(str(file))

    assert len(docs) == 1

    assert "print('hello')" in docs[0].page_content

    assert docs[0].metadata["type"] == "python"
