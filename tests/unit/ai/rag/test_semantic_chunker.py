from backend.app.ai.rag.pipeline.semantic_chunker import (
    SemanticChunker,
)


def test_semantic_chunker_init():
    chunker = SemanticChunker()

    assert chunker.similarity_threshold == 0.3


def test_sentence_split():
    chunker = SemanticChunker()

    sentences = chunker._split_sentences("Python很好。它很流行。")

    assert len(sentences) == 2


def test_semantic_split():
    chunker = SemanticChunker(
        similarity_threshold=0.2,
    )

    chunks = chunker.split(
        """
        Python是一种编程语言。
        Python拥有大量库。
        火星距离地球很远。
        """
    )

    assert len(chunks) == 2

    assert chunks[0].metadata["type"] == "semantic"
