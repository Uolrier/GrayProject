"""
Rate limiting utilities.

Provides token bucket based rate limiter.
"""

import time
from threading import Lock

from backend.app.core.exceptions import RateLimitExceeded


class RateLimiter:
    """
    Token Bucket Rate Limiter.

    Args:
        capacity:
            Maximum number of tokens.

        refill_rate:
            Token refill rate per second.
    """

    def __init__(
        self,
        capacity: int,
        refill_rate: float,
    ):
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")

        if refill_rate < 0:
            raise ValueError("refill_rate cannot be negative")

        self.capacity = float(capacity)
        self.tokens = float(capacity)

        self.refill_rate = float(refill_rate)

        self.last_refill = time.time()

        self.lock = Lock()

    def allow(self) -> bool:
        """
        Check whether a request is allowed.

        Returns:
            True:
                request accepted.

            False:
                request rejected.
        """

        with self.lock:
            self._refill()

            if self.tokens >= 1:
                self.tokens -= 1
                return True

            return False

    def _refill(self):
        """
        Refill tokens according to elapsed time.
        """

        now = time.time()

        elapsed = now - self.last_refill

        if elapsed <= 0:
            return

        refill_amount = elapsed * self.refill_rate

        self.tokens = min(
            self.capacity,
            self.tokens + refill_amount,
        )

        self.last_refill = now

    def check(self):
        """
        Raise RateLimitExceeded if request is rejected.
        """

        if not self.allow():
            raise RateLimitExceeded()
