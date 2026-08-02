"""
Network timeout configuration.

Provides unified timeout and retry settings.
"""

from dataclasses import dataclass

from config.settings import load_network_config


@dataclass
class TimeoutConfig:
    """
    Request timeout configuration.
    """

    connect: float = 5

    read: float = 60

    total: float = 65


@dataclass
class RetryConfig:
    """
    Retry configuration.
    """

    max_attempts: int = 3

    backoff_factor: float = 1


def get_timeout_config() -> TimeoutConfig:
    """
    Load timeout configuration.
    """

    config = load_network_config()

    timeout = config.get(
        "timeout",
        {},
    )

    return TimeoutConfig(
        connect=timeout.get(
            "connect",
            5,
        ),
        read=timeout.get(
            "read",
            60,
        ),
        total=timeout.get(
            "total",
            65,
        ),
    )


def get_retry_config() -> RetryConfig:
    """
    Load retry configuration.
    """

    config = load_network_config()

    retry = config.get(
        "retry",
        {},
    )

    return RetryConfig(
        max_attempts=retry.get(
            "max_attempts",
            3,
        ),
        backoff_factor=retry.get(
            "backoff_factor",
            1,
        ),
    )
