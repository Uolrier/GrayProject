from backend.app.security.rules import INJECTION_PATTERNS


class PromptInjectionDetector:
    """
    Detect potential prompt injection attacks.
    """

    def __init__(self, rules=None):
        self.rules = rules or INJECTION_PATTERNS

    def detect(self, text: str) -> bool:
        """
        Return True when injection pattern is detected.
        """

        if not text:
            return False

        normalized_text = text.lower()

        for pattern in self.rules:
            if pattern.lower() in normalized_text:
                return True

        return False
