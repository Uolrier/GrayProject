from app.ai.rag.collection import (
    CollectionManager,
)


def test_create_collection():
    manager = CollectionManager()

    collection = manager.create(
        "test_docs",
        description="test collection",
    )

    assert collection.name == "test_docs"

    assert manager.get("test_docs") == collection


def test_delete_collection():
    manager = CollectionManager()

    manager.create("temp")

    removed = manager.delete("temp")

    assert removed.name == "temp"

    assert manager.get("temp") is None


def test_list_collection():
    manager = CollectionManager()

    manager.create("a")
    manager.create("b")

    result = manager.list()

    assert len(result) == 2
