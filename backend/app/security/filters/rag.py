from typing import List

from backend.app.ai.rag.ingestion.schema import Document
from backend.app.security.base import BaseSecurityFilter
from backend.app.security.rules import INJECTION_PATTERNS
from backend.app.security.schema import SecurityResult


class RAGInjectionFilter(BaseSecurityFilter):
    """
    Detect prompt injection inside RAG documents.
    """

    name = "rag_injection"

    def __init__(self, rules=None):
        self.rules = rules or INJECTION_PATTERNS

    def check(self, data: Document) -> SecurityResult:
        """
        Check a single document.
        """

        if not data:
            return SecurityResult(passed=True)

        content = getattr(
            data,
            "page_content",
            None,
        )

        if content is None:
            content = getattr(
                data,
                "content",
                "",
            )

        if not content:
            return SecurityResult(passed=True)

        normalized_text = content.lower()

        matched_rules = []

        for pattern in self.rules:
            if pattern.lower() in normalized_text:
                matched_rules.append(pattern)

        if matched_rules:
            return SecurityResult(
                passed=False,
                score=float(len(matched_rules)),
                matched_rules=matched_rules,
                reason="RAG document injection detected",
            )

        return SecurityResult(passed=True)

    def filter(self, data: List[Document]) -> List[Document]:
        """
        Remove dangerous documents.
        """

        safe_documents = []

        for document in data:
            result = self.check(document)

            if result.passed:
                safe_documents.append(document)

        return safe_documents
