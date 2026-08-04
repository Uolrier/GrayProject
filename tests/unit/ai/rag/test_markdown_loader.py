from backend.app.ai.rag.ingestion.factory import LoaderFactory


def test_markdown_loader_registered():
    assert "markdown" in LoaderFactory.list_loaders()
    assert "md" in LoaderFactory.list_loaders()


def test_markdown_loader(tmp_path):
    file = tmp_path / "demo.md"

    file.write_text("# GrayProject\n\nRAG Test", encoding="utf-8")

    loader = LoaderFactory.create(
        "markdown",
        path=str(file),
    )

    docs = loader.load()

    assert len(docs) == 1
    assert "# GrayProject" in docs[0].page_content
    assert docs[0].metadata["type"] == "markdown"
