from typing import List

from backend.app.ai.rag.ingestion.schema import Document
from config.settings import load_security_config

from .filters.input import InputInjectionFilter
from .filters.rag import RAGInjectionFilter
from .schema import SecurityResult


class SecurityManager:
    """
    Central manager for security pipeline.
    """

    def __init__(
        self,
        input_filter=None,
        rag_filter=None,
        config=None,
    ):
        if config is None:
            config = load_security_config()

        security_config = config.get("security", {})

        security_enabled = security_config.get("enabled", True)

        if not security_enabled:
            self.input_filter = None
            self.rag_filter = None
            return

        filters = security_config.get("filters", {})

        input_enabled = filters.get("input_injection", {}).get("enabled", True)

        rag_enabled = filters.get("rag_injection", {}).get("enabled", True)

        self.input_filter = None

        self.rag_filter = None

        if input_enabled:
            self.input_filter = input_filter or InputInjectionFilter()

        if rag_enabled:
            self.rag_filter = rag_filter or RAGInjectionFilter()

    def check_input(
        self,
        text: str,
    ) -> SecurityResult:
        """
        Check user input.
        """

        if self.input_filter is None:
            return SecurityResult(passed=True)

        return self.input_filter.check(text)

    def filter_documents(
        self,
        documents: List[Document],
    ) -> List[Document]:
        """
        Filter RAG documents.
        """

        if self.rag_filter is None:
            return documents

        return self.rag_filter.filter(documents)
