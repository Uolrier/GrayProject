"""
GrayProject 全局配置加载器

统一管理：

- 环境变量
- 项目路径
- 服务配置
- AI模型配置
- YAML配置加载
"""

import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

# ==========================
# 项目根目录
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================
# 加载 .env
# ==========================

ENV_PATH = BASE_DIR / ".env"

if ENV_PATH.exists():
    load_dotenv(ENV_PATH)


# ==========================
# YAML 配置路径
# ==========================

MODEL_CONFIG_PATH = BASE_DIR / "config" / "models.yaml"

NETWORK_CONFIG_PATH = BASE_DIR / "config" / "network.yaml"

SECURITY_CONFIG_PATH = BASE_DIR / "config" / "security.yaml"

EMBEDDING_CONFIG_PATH = BASE_DIR / "config" / "embedding.yaml"

TOKENIZER_CONFIG_PATH = BASE_DIR / "config" / "tokenizer.yaml"

VECTORDB_CONFIG_PATH = BASE_DIR / "config" / "vectordb.yaml"

# ==========================
# YAML 加载函数
# ==========================


def load_vectordb_config():
    return load_yaml(
        VECTORDB_CONFIG_PATH,
    )


def load_yaml(path: Path):
    """
    Generic YAML loader.
    """

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as f:
        return yaml.safe_load(f)


def load_model_config():
    return load_yaml(
        MODEL_CONFIG_PATH,
    )


def load_network_config():
    return load_yaml(
        NETWORK_CONFIG_PATH,
    )


def load_security_config():
    return load_yaml(
        SECURITY_CONFIG_PATH,
    )


def load_embedding_config():
    return load_yaml(
        EMBEDDING_CONFIG_PATH,
    )


# ==========================
# 全局配置类
# ==========================


class Settings:
    """
    GrayProject 全局配置
    """

    # ==========================
    # Project
    # ==========================

    PROJECT_NAME = os.getenv(
        "PROJECT_NAME",
        "GrayProject",
    )

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development",
    )

    # ==========================
    # Backend
    # ==========================

    BACKEND_HOST = os.getenv(
        "BACKEND_HOST",
        "127.0.0.1",
    )

    BACKEND_PORT = int(
        os.getenv(
            "BACKEND_PORT",
            8000,
        )
    )

    # ==========================
    # Database
    # ==========================

    DB_HOST = os.getenv(
        "DB_HOST",
        "localhost",
    )

    DB_PORT = int(
        os.getenv(
            "DB_PORT",
            3306,
        )
    )

    DB_NAME = os.getenv(
        "DB_NAME",
        "grayproject",
    )

    DB_USER = os.getenv(
        "DB_USER",
        "root",
    )

    DB_PASSWORD = os.getenv(
        "DB_PASSWORD",
        "",
    )

    # ==========================
    # Path
    # ==========================

    DATA_DIR = BASE_DIR / "data"

    MODEL_DIR = BASE_DIR / "models"

    MODEL_PATH = os.getenv(
        "MODEL_PATH",
        "./models",
    )

    # ==========================
    # Logging
    # ==========================

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO",
    )

    # ==========================
    # Embedding
    # ==========================

    OPENAI_EMBEDDING_MODEL = os.getenv(
        "OPENAI_EMBEDDING_MODEL",
        "text-embedding-3-small",
    )

    @property
    def embedding_provider(self):
        """
        Get embedding provider.

        Example:
            bge
        """

        config = load_embedding_config()

        return config["embedding"]["provider"]

    @property
    def embedding_model(self):
        """
        Get embedding model name.
        """

        config = load_embedding_config()

        return config["embedding"]["model"]

    @property
    def embedding_dimension(self):
        """
        Get embedding dimension.
        """

        config = load_embedding_config()

        return config["embedding"]["dimension"]

    # ==========================
    # OpenAI
    # ==========================

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        "",
    )

    OPENAI_BASE_URL = os.getenv(
        "OPENAI_BASE_URL",
        None,
    )

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-4.1-mini",
    )

    # ==========================
    # DeepSeek
    # ==========================

    DEEPSEEK_API_KEY = os.getenv(
        "DEEPSEEK_API_KEY",
        "",
    )

    DEEPSEEK_MODEL = os.getenv(
        "DEEPSEEK_MODEL",
        "deepseek-chat",
    )

    # ==========================
    # Config Path
    # ==========================

    TOKENIZER_CONFIG_PATH = TOKENIZER_CONFIG_PATH

    NETWORK_CONFIG_PATH = NETWORK_CONFIG_PATH

    SECURITY_CONFIG_PATH = SECURITY_CONFIG_PATH

    EMBEDDING_CONFIG_PATH = EMBEDDING_CONFIG_PATH


# ==========================
# 单例
# ==========================


settings = Settings()
