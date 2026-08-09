from app.ai.rag.ingestion.factory import LoaderFactory


def test_text_loader(tmp_path):
    file = tmp_path / "test.txt"

    file.write_text("Hello GrayProject", encoding="utf-8")

    loader = LoaderFactory.create("text", path=str(file))

    docs = loader.load()

    assert len(docs) == 1

    assert docs[0].page_content == "Hello GrayProject"

    assert docs[0].metadata["type"] == "txt"

    assert docs[0].metadata["source"] == str(file)


def test_text_loader_streaming(tmp_path):
    file = tmp_path / "large.txt"

    file.write_text(
        "a" * 100,
        encoding="utf-8",
    )

    loader = LoaderFactory.create(
        "text",
        path=str(file),
        chunk_size=20,
    )

    docs = list(loader.iter_load())

    assert len(docs) == 5
    assert all(len(doc.page_content) <= 20 for doc in docs)

    assert "".join(doc.page_content for doc in docs) == "a" * 100
