from unittest.mock import patch

import pytest

from backend.app.llm.factory import ModelManager
from backend.app.llm.providers.deepseek import DeepSeekLLM
from backend.app.llm.providers.openai_llm import OpenAILLM
from backend.app.runtime.dummy import DummyRuntime
from backend.app.runtime.huggingface import HuggingFaceRuntime


@patch("backend.app.llm.factory.ProviderConfig.get")
def test_create_openai(mock_config):
    mock_config.return_value = {
        "api_key": "fake-key",
        "model": "gpt-test",
    }

    model = ModelManager.create("openai")

    assert type(model) is OpenAILLM
    assert model.api_key == "fake-key"
    assert model.model_name == "gpt-test"


@patch("backend.app.llm.factory.ProviderConfig.get")
def test_create_deepseek(mock_config):
    mock_config.return_value = {
        "api_key": "fake-deepseek-key",
        "model": "deepseek-test",
        "base_url": "https://test.example.com",
    }

    model = ModelManager.create("deepseek")

    assert type(model) is DeepSeekLLM
    assert model.api_key == "fake-deepseek-key"
    assert model.base_url == "https://test.example.com"


def test_create_huggingface():
    runtime = ModelManager.create("huggingface")
    assert isinstance(runtime, HuggingFaceRuntime)


def test_create_dummy():
    runtime = ModelManager.create("dummy")
    assert isinstance(runtime, DummyRuntime)


def test_unknown_model():
    with pytest.raises(ValueError, match="Model 'unknown' is not registered"):
        ModelManager.create("unknown")


@patch("backend.app.llm.factory.load_model_config")
@patch("backend.app.llm.factory.ProviderConfig.get")
def test_create_active(mock_provider, mock_load_config):
    mock_provider.return_value = {
        "api_key": "fake-key",
        "model": "deepseek-test",
        "base_url": "https://test.example.com",
    }

    mock_load_config.return_value = {"active_model": "deepseek"}

    model = ModelManager.create_active()

    assert type(model) is DeepSeekLLM


@patch("backend.app.llm.factory.ProviderConfig.get")
def test_switch_models(mock_config):
    mock_config.return_value = {
        "api_key": "fake-key",
        "model": "test-model",
        "base_url": "https://test.example.com",
    }

    m1 = ModelManager.create("openai")
    m2 = ModelManager.create("deepseek")
    m3 = ModelManager.create("dummy")
    m4 = ModelManager.create("huggingface")
    m5 = ModelManager.create("openai")

    assert isinstance(m1, OpenAILLM)
    assert isinstance(m2, DeepSeekLLM)
    assert isinstance(m3, DummyRuntime)
    assert isinstance(m4, HuggingFaceRuntime)
    assert isinstance(m5, OpenAILLM)

    assert m1 is not m5


def test_create_returns_new_instance():
    a = ModelManager.create("dummy")
    b = ModelManager.create("dummy")

    assert a is not b

    a = ModelManager.create("openai")
    b = ModelManager.create("openai")

    assert a is not b
