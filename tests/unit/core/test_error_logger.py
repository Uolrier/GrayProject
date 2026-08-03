from unittest.mock import patch

from backend.app.core.error_logger import ErrorLogger


def test_log_exception():
    """
    Log basic exception.
    """

    with patch("backend.app.core.error_logger.logger.error") as mock_error:
        try:
            raise ValueError("test error")
        except ValueError as e:
            ErrorLogger.log(e)

    assert mock_error.called

    message = mock_error.call_args[0][0]

    assert "ValueError" in message
    assert "test error" in message


def test_log_context():
    """
    Log exception with context.
    """

    with patch("backend.app.core.error_logger.logger.error") as mock_error:
        try:
            raise RuntimeError("failed")
        except RuntimeError as e:
            ErrorLogger.log(
                e,
                {
                    "provider": "openai",
                    "model": "gpt-4",
                },
            )

    message = mock_error.call_args[0][0]

    assert "provider: openai" in message
    assert "model: gpt-4" in message


def test_log_without_context():
    """
    Context is optional.
    """

    with patch("backend.app.core.error_logger.logger.error") as mock_error:
        try:
            raise RuntimeError("failed")
        except RuntimeError as e:
            ErrorLogger.log(e)

    message = mock_error.call_args[0][0]

    assert "Context" in message
    assert "None" in message


def test_log_traceback():
    """
    Traceback should be included.
    """

    with patch("backend.app.core.error_logger.logger.error") as mock_error:
        try:
            raise ValueError("traceback")
        except ValueError as e:
            ErrorLogger.log(e)

    message = mock_error.call_args[0][0]

    assert "Traceback" in message
    assert "raise ValueError" in message
