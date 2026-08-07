from app.ai.rag.ingestion.directory import (
    DirectoryImporter,
)


def test_directory_import_text(tmp_path):
    file = tmp_path / "hello.txt"

    file.write_text(
        "hello rag",
        encoding="utf-8",
    )

    importer = DirectoryImporter()

    docs = importer.import_directory(tmp_path)

    assert len(docs) == 1

    assert docs[0].page_content == "hello rag"

    assert docs[0].metadata["type"] == "txt"
