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
