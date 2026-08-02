from backend.app.core.exceptions import (
    GenerationError,
    ModelLoadError,
    PromptInjectionDetected,
    ProviderError,
    ValidationError,
)


def test_validation_error():
    exc = ValidationError()

    assert exc.code == "API_VALIDATION_ERROR"
    assert exc.status_code == 422
    assert exc.message == "Validation error"


def test_provider_error():
    exc = ProviderError(
        "DeepSeek unavailable",
    )

    assert exc.code == "LLM_PROVIDER_ERROR"
    assert exc.message == "DeepSeek unavailable"


def test_generation_error():
    exc = GenerationError()

    assert exc.code == "LLM_GENERATION_ERROR"


def test_model_load_error():
    exc = ModelLoadError()

    assert exc.code == "RUNTIME_MODEL_LOAD_ERROR"


def test_prompt_injection_detected():
    exc = PromptInjectionDetected()

    assert exc.code == "SECURITY_PROMPT_INJECTION"
