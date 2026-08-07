from backend.app.security.base import BaseSecurityFilter
from backend.app.security.rules import INJECTION_PATTERNS
from backend.app.security.schema import SecurityResult


class InputInjectionFilter(BaseSecurityFilter):
    """
    Detect prompt injection from user input.
    """

    name = "input_injection"

    def __init__(self, rules=None):
        self.rules = rules or INJECTION_PATTERNS

    def check(self, data: str) -> SecurityResult:
        """
        Check user input for injection patterns.
        """

        if not data:
            return SecurityResult(passed=True)

        normalized_text = data.lower()

        matched_rules = []

        for pattern in self.rules:
            if pattern.lower() in normalized_text:
                matched_rules.append(pattern)

        if matched_rules:
            return SecurityResult(
                passed=False,
                score=float(len(matched_rules)),
                matched_rules=matched_rules,
                reason="Prompt injection detected",
            )

        return SecurityResult(passed=True)

    def filter(self, data: str):
        """
        Return input if safe.

        Dangerous input will return None.
        """

        result = self.check(data)

        if result.passed:
            return data

        return None
