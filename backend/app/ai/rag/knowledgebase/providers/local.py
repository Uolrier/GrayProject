from app.ai.embeddings.factory import EmbeddingFactory
from app.ai.rag.ingestion.factory import LoaderFactory
from app.ai.rag.pipeline.index_pipeline import IndexPipeline
from app.ai.rag.retrieval.vector_retriever import VectorRetriever
from app.ai.rag.vectorstore.factory import VectorStoreFactory

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

        self.vector_store.delete_collection(self.config.name)

    def rebuild(self):
        """
        Rebuild knowledge base.
        """

        raise NotImplementedError
