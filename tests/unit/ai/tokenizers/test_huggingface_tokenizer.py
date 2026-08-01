from unittest.mock import MagicMock, patch


@patch("backend.app.ai.tokenizers.providers.huggingface_tokenizer.AutoTokenizer")
def test_encode(
    mock_tokenizer,
):
    instance = MagicMock()

    instance.encode.return_value = [
        1,
        2,
        3,
    ]

    mock_tokenizer.from_pretrained.return_value = instance

    from backend.app.ai.tokenizers.providers.huggingface_tokenizer import (
        HuggingFaceTokenizer,
    )

    tokenizer = HuggingFaceTokenizer()

    result = tokenizer.encode("hello")

    assert result == [
        1,
        2,
        3,
    ]
