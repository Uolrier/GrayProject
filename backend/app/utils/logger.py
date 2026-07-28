import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(app):

    log_dir = "logs"

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)


    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )


    # 文件日志
    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=1024 * 1024 * 10,
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)



    # 控制台日志
    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)



    app.logger.setLevel(logging.INFO)


    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)


    app.logger.info(
        "Logger initialized"
    )

    return app