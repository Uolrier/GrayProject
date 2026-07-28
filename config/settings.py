"""
GrayProject 全局配置加载器

统一管理：
- 环境变量
- 项目路径
- 服务配置
"""


import os
from pathlib import Path
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
# 全局配置类
# ==========================


class Settings:
    """
    GrayProject 全局配置
    """

    # 项目
    PROJECT_NAME = os.getenv(
        "PROJECT_NAME",
        "GrayProject"
    )


    # 环境
    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development"
    )


    # Backend

    BACKEND_HOST = os.getenv(
        "BACKEND_HOST",
        "127.0.0.1"
    )


    BACKEND_PORT = int(
        os.getenv(
            "BACKEND_PORT",
            8000
        )
    )


    # 数据目录

    DATA_DIR = BASE_DIR / "data"


    # 模型目录

    MODEL_DIR = BASE_DIR / "models"


    # 日志

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )


# 单例配置对象

settings = Settings()