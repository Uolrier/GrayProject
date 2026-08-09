from backend.app.ai.rag.ingestion.schema import (
    Document,
)
from backend.app.ai.rag.pipeline.index_pipeline import (
    IndexPipeline,
)
from backend.app.ai.rag.vectorstore.chroma import (
    ChromaVectorStore,
)


class DummyEmbedding:
    """
    Simple deterministic embedding.

    Used only for evaluation framework testing.
    """

    def _embed(
        self,
        text: str,
    ):
        value = len(text) % 10

        return [
            value / 10,
            0.1,
            0.2,
        ]

    def embed_text(
        self,
        text: str,
    ):
        return self._embed(text)

    def embed_documents(
        self,
        texts: list[str],
    ):
        return [self._embed(text) for text in texts]


def build_eval_documents():
    return [
        Document(
            page_content="""
            class VectorRetriever:

            Retriever based on vector similarity search.

            It converts query text into embedding
            and searches vector store.
            """,
            metadata={"source": "backend/app/ai/rag/retrieval/vector_retriever.py"},
        ),
        Document(
            page_content="""
            class KnowledgeBaseManager:

            Responsible for creating knowledge bases,
            storing instances and retrieving instances.
            """,
            metadata={"source": "backend/app/ai/rag/knowledgebase/manager.py"},
        ),
        Document(
            page_content="""
            class IndexPipeline:

            Document indexing pipeline.

            Flow:

            Document
            Chunking
            Embedding
            Vector Store
            """,
            metadata={"source": "backend/app/ai/rag/pipeline/index_pipeline.py"},
        ),
        Document(
            page_content="""
            class ChromaVectorStore:

            Persistent vector database.

            Supports add and query operations.
            """,
            metadata={"source": "backend/app/ai/rag/vectorstore/chroma.py"},
        ),
        Document(
            page_content="""
            class QueryPipeline:

            Query processing pipeline.

            Retriever
            Reranker
            SourceBuilder
            QueryResponse
            """,
            metadata={"source": "backend/app/ai/rag/query/pipeline.py"},
        ),
    ]


def build_eval_vector_store():
    store = ChromaVectorStore(
        persist_dir="tests/evaluation/rag/.chroma",
        collection_name="eval_grayproject",
    )

    embedding = DummyEmbedding()

    pipeline = IndexPipeline(
        embedding=embedding,
        vector_store=store,
        collection_name="eval_grayproject",
    )

    documents = build_eval_documents()

    pipeline.run(documents)

    return store
