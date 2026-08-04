import json

from backend.app.ai.rag.ingestion.loaders.json import JSONDocumentLoader


def test_json_loader_basic(tmp_path):
    file = tmp_path / "test.json"

    file.write_text(
        json.dumps({"content": "hello json", "source": "test"}), encoding="utf-8"
    )

    loader = JSONDocumentLoader()

    docs = loader.load(str(file))

    assert len(docs) == 1
    assert docs[0].page_content == "hello json"
    assert docs[0].metadata["source"] == "test"


def test_json_loader_list(tmp_path):
    file = tmp_path / "list.json"

    file.write_text(
        json.dumps([{"content": "doc1"}, {"content": "doc2"}]), encoding="utf-8"
    )

    loader = JSONDocumentLoader()

    docs = loader.load(str(file))

    assert len(docs) == 2
    assert docs[0].page_content == "doc1"
    assert docs[1].page_content == "doc2"


def test_json_loader_object(tmp_path):
    file = tmp_path / "object.json"

    file.write_text(json.dumps({"name": "Gray", "type": "AI"}), encoding="utf-8")

    loader = JSONDocumentLoader()

    docs = loader.load(str(file))

    assert len(docs) == 1
    assert "name: Gray" in docs[0].page_content
