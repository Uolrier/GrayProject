from backend.app.ai.rag.chat.service import RagChatService
from backend.app.ai.rag.context import SimpleContextBuilder
from backend.app.ai.rag.knowledgebase.manager import KnowledgeBaseManager
from backend.app.ai.rag.query import QueryPipeline
from backend.app.ai.rag.query.service import QueryService


class RAGRuntimeManager:
    """
    Build RAG application runtime from a knowledge base.
    """

    @classmethod
    def create_chat_service(
        cls,
        knowledge_base_manager: KnowledgeBaseManager,
        knowledge_base_name: str,
    ):
        knowledge_base = knowledge_base_manager.get(
            knowledge_base_name,
        )

        retriever = knowledge_base.retriever

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
