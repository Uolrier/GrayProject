import os

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
