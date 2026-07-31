class GrayException(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

        super().__init__(message)


class SecurityException(GrayException):
    """
    Base exception for security related errors.
    """

    pass


class PromptInjectionDetected(SecurityException):
    """
    Raised when prompt injection is detected.
    """

    def __init__(
        self,
        message: str = "Potential prompt injection detected",
    ):
        super().__init__(
            code="SECURITY_PROMPT_INJECTION",
            message=message,
        )
