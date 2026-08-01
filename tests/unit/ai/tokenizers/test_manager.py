from unittest.mock import MagicMock, patch


@patch("backend.app.ai.tokenizers.manager.TokenizerFactory.create")
def test_create_default_tokenizer(
    mock_create,
):
    mock_create.return_value = MagicMock()

    from backend.app.ai.tokenizers.manager import (
        TokenizerManager,
    )

    manager = TokenizerManager()

    tokenizer = manager.create_default()

    assert tokenizer is not None

    mock_create.assert_called_once()
