import logging
import os
import sys
from logging.handlers import RotatingFileHandler


def setup_logger():
    """
    初始化 GrayProject 日志系统
    """

    logger = logging.getLogger("GrayProject")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")

    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # 文件日志目录
    log_dir = "logs"

    os.makedirs(log_dir, exist_ok=True)

    # 文件日志
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, "app.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()
