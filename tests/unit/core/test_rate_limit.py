import time

import pytest

from backend.app.core.exceptions import RateLimitExceeded
from backend.app.core.rate_limit import RateLimiter


def test_check_success():
    limiter = RateLimiter(
        capacity=1,
        refill_rate=0,
    )

    limiter.check()


def test_check_raise():
    limiter = RateLimiter(
        capacity=1,
        refill_rate=0,
    )

    limiter.check()

    with pytest.raises(RateLimitExceeded):
        limiter.check()


def test_rate_limiter_allows_requests():
    limiter = RateLimiter(
        capacity=2,
        refill_rate=0,
    )

    assert limiter.allow()
    assert limiter.allow()


def test_rate_limiter_blocks_when_empty():
    limiter = RateLimiter(
        capacity=1,
        refill_rate=0,
    )

    assert limiter.allow()

    assert not limiter.allow()


def test_rate_limiter_refills():
    limiter = RateLimiter(
        capacity=1,
        refill_rate=10,
    )

    assert limiter.allow()

    time.sleep(0.2)

    assert limiter.allow()


def test_invalid_capacity():
    with pytest.raises(ValueError):
        RateLimiter(
            capacity=0,
            refill_rate=1,
        )


def test_invalid_refill_rate():
    with pytest.raises(ValueError):
        RateLimiter(
            capacity=1,
            refill_rate=-1,
        )
