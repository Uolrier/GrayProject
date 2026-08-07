from pathlib import Path

from app.ai.embeddings.factory import EmbeddingFactory
from app.ai.rag.incremental.manager import IncrementalManager
from app.ai.rag.incremental.scanner import FileScanner
from app.ai.rag.incremental.tracker import FileTracker
from app.ai.rag.ingestion.directory import DirectoryImporter
from app.ai.rag.ingestion.factory import LoaderFactory
from app.ai.rag.pipeline.index_pipeline import IndexPipeline
from app.ai.rag.retrieval.vector_retriever import VectorRetriever
from app.ai.rag.vectorstore.factory import VectorStoreFactory
from app.ai.rag.watcher.local import LocalWatcher

from ..base import BaseKnowledgeBase
from ..schema import (
    KnowledgeBaseConfig,
    KnowledgeBaseSearchResult,
)


class LocalKnowledgeBase(BaseKnowledgeBase):
    """
    Local knowledge base implementation.
    """

    def __init__(
        self,
        config: KnowledgeBaseConfig,
    ):
        self.directory_importer = DirectoryImporter()

        self.incremental_manager = None

        self.watcher = None

        self.config = config

        self.embedding = EmbeddingFactory.create(config.embedding)

        self.vector_store = VectorStoreFactory.create(config.vectordb)

        self.index_pipeline = IndexPipeline(
            embedding=self.embedding,
            vector_store=self.vector_store,
            collection_name=config.name,
        )

        self.retriever = VectorRetriever(
            embedding=self.embedding,
            vector_store=self.vector_store,
        )

    def add(
        self,
        path: str,
        loader_type: str,
    ):
        """
        Add documents into knowledge base.
        """

        loader = LoaderFactory.create(
            loader_type,
            path=path,
        )

        documents = loader.load()

        return self.index_pipeline.run(documents)

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):
        """
        Search knowledge base.
        """

        documents = self.retriever.search(
            query=query,
            top_k=top_k,
        )

        return KnowledgeBaseSearchResult(
            query=query,
            documents=documents,
            metadata={
                "knowledge_base": self.config.name,
            },
        )

    def delete(self):
        """
        Delete knowledge base.
        """

        self.disable_auto_update()

        self.vector_store.delete_collection(self.config.name)

    def rebuild(self):
        """
        Rebuild knowledge base.
        """

        raise NotImplementedError

    def enable_auto_update(self):
        if not self.config.root_path:
            raise ValueError("root_path required")

        scanner = FileScanner(
            root_path=self.config.root_path,
        )

        tracker = FileTracker(storage_path=f".gray/tracker/{self.config.name}.json")

        self.incremental_manager = IncrementalManager(
            scanner=scanner,
            tracker=tracker,
            document_loader=self._load_document,
            pipeline=self.index_pipeline,
        )

        self.watcher = LocalWatcher(
            incremental_manager=self.incremental_manager,
            interval=self.config.watch_interval,
        )

        self.watcher.start()

    def disable_auto_update(self):
        if self.watcher:
            self.watcher.stop()

    def _load_document(
        self,
        path: str,
    ):
        """
        Load document automatically.
        """

        path_obj = Path(path)

        if path_obj.is_dir():
            return self.directory_importer.import_directory(path_obj)

        loader_name = self.directory_importer._get_loader_name(path_obj)

        if loader_name is None:
            return []

        loader = LoaderFactory.create(
            loader_name,
            path=str(path_obj),
        )

        return loader.load()
