from unittest.mock import MagicMock, patch

from app.ai.rag.knowledgebase.providers.local import (
    LocalKnowledgeBase,
)
from app.ai.rag.knowledgebase.registry import (
    KnowledgeBaseRegistry,
)
from app.ai.rag.knowledgebase.schema import (
    KnowledgeBaseConfig,
)


def test_knowledge_base_registry():
    registry = KnowledgeBaseRegistry()

    registry.register(
        "local",
        LocalKnowledgeBase,
    )

    assert registry.contains("local")

    assert registry.get("local") == LocalKnowledgeBase

    assert "local" in registry.list()


def test_local_knowledge_base_create():
    config = KnowledgeBaseConfig(
        name="test",
        type="local",
        embedding="bge",
        vectordb="chroma",
    )

    with (
        patch(
            "app.ai.rag.knowledgebase.providers.local.EmbeddingFactory.create"
        ) as embedding_mock,
        patch(
            "app.ai.rag.knowledgebase.providers.local.VectorStoreFactory.create"
        ) as store_mock,
    ):
        embedding_mock.return_value = MagicMock()

        store_mock.return_value = MagicMock()

        kb = LocalKnowledgeBase(config)

        assert kb.config.name == "test"

        assert kb.embedding is not None

        assert kb.vector_store is not None


def test_local_knowledge_base_add():
    config = KnowledgeBaseConfig(
        name="test",
        type="local",
        embedding="bge",
        vectordb="chroma",
    )

    with (
        patch("app.ai.rag.knowledgebase.providers.local.EmbeddingFactory.create"),
        patch("app.ai.rag.knowledgebase.providers.local.VectorStoreFactory.create"),
    ):
        kb = LocalKnowledgeBase(config)

        kb.index_pipeline = MagicMock()

        loader = MagicMock()

        loader.load.return_value = ["document"]

        with patch(
            "app.ai.rag.knowledgebase.providers.local.LoaderFactory.create",
            return_value=loader,
        ):
            kb.add(
                path="demo.txt",
            )

            loader.load.assert_called_once()

            kb.index_pipeline.run.assert_called_once()


def test_local_knowledge_base_search():
    config = KnowledgeBaseConfig(
        name="test",
        type="local",
        embedding="bge",
        vectordb="chroma",
    )

    with (
        patch("app.ai.rag.knowledgebase.providers.local.EmbeddingFactory.create"),
        patch("app.ai.rag.knowledgebase.providers.local.VectorStoreFactory.create"),
    ):
        kb = LocalKnowledgeBase(config)

        kb.retriever = MagicMock()

        kb.retriever.search.return_value = []

        result = kb.search("hello")

        assert result.query == "hello"

        assert result.documents == []


def test_local_knowledge_base_delete():
    config = KnowledgeBaseConfig(
        name="test",
        type="local",
        embedding="bge",
        vectordb="chroma",
    )

    with (
        patch("app.ai.rag.knowledgebase.providers.local.EmbeddingFactory.create"),
        patch("app.ai.rag.knowledgebase.providers.local.VectorStoreFactory.create"),
    ):
        store = MagicMock()

        with patch(
            "app.ai.rag.knowledgebase.providers.local.VectorStoreFactory.create",
            return_value=store,
        ):
            kb = LocalKnowledgeBase(config)

            kb.delete()

            store.delete_collection.assert_called_once_with("test")


def test_local_knowledge_base_auto_update():
    config = KnowledgeBaseConfig(
        name="test",
        type="local",
        embedding="bge",
        vectordb="chroma",
        root_path="demo",
        auto_update=True,
        watch_interval=10,
    )

    with (
        patch("app.ai.rag.knowledgebase.providers.local.EmbeddingFactory.create"),
        patch("app.ai.rag.knowledgebase.providers.local.VectorStoreFactory.create"),
    ):
        kb = LocalKnowledgeBase(config)

        kb.enable_auto_update()

        assert kb.incremental_manager is not None

        assert kb.watcher is not None

        kb.watcher.stop()


def test_local_knowledge_base_disable_auto_update():
    config = KnowledgeBaseConfig(
        name="test",
        type="local",
        embedding="bge",
        vectordb="chroma",
        root_path="demo",
    )

    with (
        patch("app.ai.rag.knowledgebase.providers.local.EmbeddingFactory.create"),
        patch("app.ai.rag.knowledgebase.providers.local.VectorStoreFactory.create"),
    ):
        kb = LocalKnowledgeBase(config)

        watcher = MagicMock()

        kb.watcher = watcher

        kb.disable_auto_update()

        watcher.stop.assert_called_once()
