import pytest

from backend.app.runtime.dummy import DummyRuntime


@pytest.fixture
def dummy_llm():
    runtime = DummyRuntime()
    runtime.load()

    return runtime
