import time
from functools import wraps
from typing import Callable, Iterable, Type


def retry(
    max_attempts: int = 3,
    backoff_factor: float = 1.0,
    exceptions: Iterable[Type[Exception]] = (Exception,),
):
    """
    Retry decorator with exponential backoff.

    Args:
        max_attempts:
            Maximum number of attempts.

        backoff_factor:
            Initial backoff delay.

        exceptions:
            Exceptions that trigger retry.
    """

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)

                except tuple(exceptions) as exc:
                    last_exception = exc

                    if attempt == max_attempts - 1:
                        raise

                    delay = backoff_factor * (2**attempt)

                    time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator
