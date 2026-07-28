import logging
import sys


def setup_logger():
    """
    初始化 GrayProject 日志系统
    """

    logger = logging.getLogger("GrayProject")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] "
        "[%(levelname)s] "
        "%(name)s: "
        "%(message)s"
    )


    console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setFormatter(formatter)


    logger.addHandler(console_handler)


    return logger


logger = setup_logger()