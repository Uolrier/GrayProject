from unittest.mock import MagicMock, patch

from backend.app.ai.tokenizers.factory import TokenizerFactory


@patch("backend.app.ai.tokenizers.providers.huggingface_tokenizer.AutoTokenizer")
def test_create_huggingface_tokenizer(
    mock_tokenizer,
):
    mock_tokenizer.from_pretrained.return_value = MagicMock()

    tokenizer = TokenizerFactory.create("huggingface")

    assert tokenizer.name == "huggingface"
