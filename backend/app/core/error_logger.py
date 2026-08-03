import traceback
from typing import Any

from backend.app.core.logger import logger


class ErrorLogger:
    """统一异常日志记录器"""

    @staticmethod
    def log(
        exception: Exception,
        context: dict[str, Any] | None = None,
    ) -> None:
        """
        Record exception with traceback and context.
        """

        context = context or {}

        context_text = "\n".join(f"{key}: {value}" for key, value in context.items())

        traceback_text = "".join(
            traceback.format_exception(
                type(exception),
                exception,
                exception.__traceback__,
            )
        )

        message = (
            "\n========== Exception ==========\n"
            f"Type: {type(exception).__name__}\n"
            f"Message: {exception}\n\n"
            "---------- Context ----------\n"
            f"{context_text or 'None'}\n\n"
            "---------- Traceback ----------\n"
            f"{traceback_text}"
            "===============================\n"
        )

        logger.error(message)
