from backend.app.security.schema import SecurityResult


def test_security_result():
    result = SecurityResult(passed=True)

    assert result.passed
