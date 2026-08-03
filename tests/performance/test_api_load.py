import concurrent.futures
import os

import pytest
from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def request_health():
    response = client.get("/api/system/health")

    return response.status_code


@pytest.mark.skipif(
    os.getenv("TESTING") != "true",
    reason="performance test only",
)
def test_health_concurrent_requests():
    """
    Concurrent health endpoint test.
    """

    total_requests = 100
    workers = 20

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(
            executor.map(
                lambda _: request_health(),
                range(total_requests),
            )
        )

    assert len(results) == total_requests

    assert all(status == 200 for status in results)
