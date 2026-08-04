from backend.app.ai.rag.ingestion.loaders.word import WordLoader


def test_word_loader(tmp_path):
    from docx import Document as DocxDocument

    file_path = tmp_path / "test.docx"

    doc = DocxDocument()

    doc.add_paragraph("GrayProject Word Loader Test")

    doc.save(file_path)

    loader = WordLoader(str(file_path))

    documents = loader.load()

    assert len(documents) == 1

    assert "GrayProject Word Loader Test" in documents[0].page_content

    assert documents[0].metadata["type"] == "word"
