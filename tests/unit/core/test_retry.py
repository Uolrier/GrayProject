from unittest.mock import patch

import pytest

from backend.app.core.retry import retry


def test_retry_success():
    """
    Function succeeds immediately.
    """

    call_count = 0

    @retry(
        max_attempts=3,
        backoff_factor=0,
    )
    def func():
        nonlocal call_count

        call_count += 1

        return "success"

    result = func()

    assert result == "success"
    assert call_count == 1


def test_retry_after_failure():
    """
    Function succeeds after retry.
    """

    call_count = 0

    @retry(
        max_attempts=3,
        backoff_factor=0,
    )
    def func():
        nonlocal call_count

        call_count += 1

        if call_count < 3:
            raise ValueError("temporary error")

        return "success"

    result = func()

    assert result == "success"
    assert call_count == 3


def test_retry_exhausted():
    """
    Retry exhausted should raise exception.
    """

    call_count = 0

    @retry(
        max_attempts=3,
        backoff_factor=0,
    )
    def func():
        nonlocal call_count

        call_count += 1

        raise ValueError("failed")

    with pytest.raises(ValueError):
        func()

    assert call_count == 3


def test_retry_backoff():
    """
    Verify exponential backoff delay.
    """

    call_count = 0

    @retry(
        max_attempts=3,
        backoff_factor=1,
    )
    def func():
        nonlocal call_count

        call_count += 1

        if call_count < 3:
            raise ValueError("temporary error")

        return "success"

    with patch("backend.app.core.retry.time.sleep") as sleep:
        result = func()

    assert result == "success"

    assert sleep.call_count == 2

    sleep.assert_any_call(1)
    sleep.assert_any_call(2)
