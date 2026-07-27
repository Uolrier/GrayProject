import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    """
    GrayProject 后端配置管理
    """

    PROJECT_NAME = os.getenv(
        "PROJECT_NAME",
        "GrayProject"
    )

    PORT = int(
        os.getenv(
            "FLASK_PORT",
            8000
        )
    )