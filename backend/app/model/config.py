from pathlib import Path

import yaml

MODEL_CONFIG_PATH = Path(__file__).parent / "models.yaml"


def load_model_config():
    """
    Load model switch config.
    """

    with open(
        MODEL_CONFIG_PATH,
        "r",
        encoding="utf-8",
    ) as f:
        return yaml.safe_load(f)
