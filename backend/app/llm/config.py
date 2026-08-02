import os
from pathlib import Path

import yaml


class ProviderConfig:
    """
    Provider configuration loader.

    Loads provider definitions from config/providers.yaml
    and resolves environment variables.
    """

    _providers = None

    @classmethod
    def _load(cls):
        if cls._providers is not None:
            return

        config_path = Path(__file__).resolve().parents[3] / "config" / "providers.yaml"

        with open(config_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        cls._providers = data.get("providers", {})

    @classmethod
    def get(cls, name: str) -> dict:
        """
        Get provider configuration.

        Args:
            name:
                Provider name.

        Returns:
            Provider configuration dictionary.
        """

        cls._load()

        if name not in cls._providers:
            return {}

        config = cls._providers[name].copy()

        api_key_env = config.get("api_key_env")

        if api_key_env:
            if isinstance(api_key_env, list):
                env_name = api_key_env[0]
            else:
                env_name = api_key_env

            config["api_key"] = os.getenv(env_name)

        return config
