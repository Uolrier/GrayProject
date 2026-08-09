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


def test_directory_import_streaming(tmp_path):
    file = tmp_path / "large.txt"

    file.write_text(
        "a" * 100,
        encoding="utf-8",
    )

    importer = DirectoryImporter()

    docs = list(importer.iter_import_directory(tmp_path))

    assert len(docs) == 1
    assert docs[0].page_content == "a" * 100


def test_directory_import_stream(tmp_path):
    file = tmp_path / "hello.txt"

    file.write_text(
        "hello rag",
        encoding="utf-8",
    )

    importer = DirectoryImporter()

    class FakePipeline:
        def __init__(self):
            self.documents = []

        def run_stream(self, documents):
            self.documents = list(documents)

            return {
                "documents": len(self.documents),
                "chunks": len(self.documents),
            }

    pipeline = FakePipeline()

    result = importer.import_directory_stream(
        tmp_path,
        pipeline,
    )

    assert result["documents"] == 1
    assert result["chunks"] == 1
    assert len(pipeline.documents) == 1
    assert pipeline.documents[0].page_content == "hello rag"
