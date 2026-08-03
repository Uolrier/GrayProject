import pytest

from config.settings import settings


@pytest.mark.integration
def test_provider_config_exists():
    assert settings is not None
