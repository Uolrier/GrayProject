from __future__ import annotations

import os  # noqa: F811
from pathlib import Path

import yaml
from dotenv import load_dotenv

# 加载 .env
load_dotenv()


class Config:
    """
    GrayProject 全局配置
    """

    PROJECT_NAME = os.getenv("PROJECT_NAME", "GrayProject")

    # Flask
    FLASK_ENV = os.getenv("FLASK_ENV", "development")

    FLASK_PORT = int(os.getenv("FLASK_PORT", 8000))

    # Database
    DB_HOST = os.getenv("DB_HOST", "localhost")

    DB_PORT = int(os.getenv("DB_PORT", 3306))

    DB_NAME = os.getenv("DB_NAME", "grayproject")

    DB_USER = os.getenv("DB_USER", "root")

    DB_PASSWORD = os.getenv("DB_PASSWORD", "")

    # AI
    MODEL_PATH = os.getenv("MODEL_PATH", "./models")

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "bge-small")

    # LLM
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")

    DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")


# 模型配置文件路径: <项目根>/config/models.yaml
# config.py 位于 backend/app/config.py
# 向上三级是项目根目录
MODEL_CONFIG_PATH = (
    Path(__file__).resolve().parent.parent.parent / "config" / "models.yaml"
)


def load_model_config():
    """
    从 YAML 加载模型切换配置。
    """
    with open(MODEL_CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
