import yaml

from config.settings import settings

from .factory import TokenizerFactory


class TokenizerManager:
    """
    Manage tokenizer instances.
    """

    def __init__(self):
        with open(
            settings.TOKENIZER_CONFIG_PATH,
            "r",
            encoding="utf-8",
        ) as f:
            self.config = yaml.safe_load(f)

    def create_default(self):
        name = self.config["default"]

        params = self.config["tokenizers"][name]

        return TokenizerFactory.create(
            name,
            **params,
        )
