from fastapi.testclient import TestClient

from backend.app.core.exceptions import ValidationError
from backend.app.main import app

client = TestClient(
    app,
    raise_server_exceptions=False,
)


@app.get("/test-validation-error")
def validation_error_route():
    raise ValidationError(
        "Invalid message",
    )


def test_gray_exception_handler():
    response = client.get(
        "/test-validation-error",
    )

    assert response.status_code == 422

    data = response.json()

    assert data["success"] is False

    assert data["error"]["code"] == ("API_VALIDATION_ERROR")

    assert data["error"]["message"] == ("Invalid message")
