from backend.app.ai.rag.source.builder import SourceBuilder


class DummyDocument:
    def __init__(self):
        self.metadata = {
            "source": "test.md",
            "chunk_id": "chunk-1",
            "page": 3,
            "line_start": 10,
            "line_end": 20,
        }

        self.score = 0.95


def test_source_builder():
    builder = SourceBuilder()

    documents = [
        DummyDocument(),
    ]

    sources = builder.build(
        documents,
    )

    assert len(sources) == 1

    assert sources[0].file_path == "test.md"

    assert sources[0].chunk_id == "chunk-1"

    assert sources[0].score == 0.95

    assert sources[0].page == 3

    assert sources[0].line_start == 10

    assert sources[0].line_end == 20
