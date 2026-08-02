class GrayException(Exception):
    """
    Base exception for GrayProject.
    """

    status_code = 500

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

        super().__init__(message)


class APIException(GrayException):
    """
    Base exception for API related errors.
    """

    status_code = 400


class ValidationError(APIException):
    """
    Invalid request parameters.
    """

    status_code = 422

    def __init__(
        self,
        message: str = "Validation error",
    ):
        super().__init__(
            code="API_VALIDATION_ERROR",
            message=message,
        )


class NotFoundError(APIException):
    """
    Resource not found.
    """

    status_code = 404

    def __init__(
        self,
        message: str = "Resource not found",
    ):
        super().__init__(
            code="API_NOT_FOUND",
            message=message,
        )


class UnauthorizedError(APIException):
    """
    Authentication failed.
    """

    status_code = 401

    def __init__(
        self,
        message: str = "Unauthorized",
    ):
        super().__init__(
            code="API_UNAUTHORIZED",
            message=message,
        )


class LLMException(GrayException):
    """
    Base exception for LLM related errors.
    """

    pass


class ProviderError(LLMException):
    """
    External provider API error.
    """

    def __init__(
        self,
        message: str = "LLM provider error",
    ):
        super().__init__(
            code="LLM_PROVIDER_ERROR",
            message=message,
        )


class GenerationError(LLMException):
    """
    Text generation failed.
    """

    def __init__(
        self,
        message: str = "Generation failed",
    ):
        super().__init__(
            code="LLM_GENERATION_ERROR",
            message=message,
        )


class LLMTimeoutError(LLMException):
    """
    LLM request timeout.
    """

    def __init__(
        self,
        message: str = "LLM request timeout",
    ):
        super().__init__(
            code="LLM_TIMEOUT_ERROR",
            message=message,
        )


class LLMRetryExhaustedError(LLMException):
    """
    LLM retry attempts exhausted.
    """

    def __init__(
        self,
        message: str = "LLM retry attempts exhausted",
    ):
        super().__init__(
            code="LLM_RETRY_EXHAUSTED",
            message=message,
        )


class RateLimitExceeded(GrayException):
    """
    Raised when request rate exceeds the configured limit.
    """

    status_code = 429

    def __init__(
        self,
        message: str = "Too many requests",
    ):
        super().__init__(
            code="RATE_LIMIT_EXCEEDED",
            message=message,
        )


class RuntimeException(GrayException):
    """
    Local model runtime errors.
    """

    pass


class ModelLoadError(RuntimeException):
    """
    Failed to load local model.
    """

    def __init__(
        self,
        message: str = "Model loading failed",
    ):
        super().__init__(
            code="RUNTIME_MODEL_LOAD_ERROR",
            message=message,
        )


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
