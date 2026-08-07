from backend.app.ai.embeddings.factory import (
    EmbeddingFactory,
)
from backend.app.ai.rag.chat.service import (
    RagChatService,
)
from backend.app.ai.rag.context import (
    SimpleContextBuilder,
)
from backend.app.ai.rag.query import (
    QueryPipeline,
)
from backend.app.ai.rag.query.service import (
    QueryService,
)
from backend.app.ai.rag.retrieval.vector_retriever import (
    VectorRetriever,
)
from backend.app.ai.rag.vectorstore.factory import (
    VectorStoreFactory,
)
from config.settings import load_embedding_config


class RAGRuntimeManager:
    """
    Build RAG application runtime.
    """

    @classmethod
    def create_chat_service(cls):
        embedding_config = load_embedding_config()

        embedding = EmbeddingFactory.create(embedding_config["embedding"]["provider"])

        vector_store = VectorStoreFactory.create(
            "chroma",
        )

        retriever = VectorRetriever(
            embedding=embedding,
            vector_store=vector_store,
        )

        context_builder = SimpleContextBuilder(
            max_chunks=5,
        )

        pipeline = QueryPipeline(
            retriever=retriever,
            context_builder=context_builder,
        )

        query_service = QueryService(
            pipeline,
        )

        return RagChatService(
            query_service=query_service,
        )
