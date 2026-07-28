"""
项目统一配置入口

后续所有模块都应从这里读取配置。
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_NAME = "GrayProject"

VERSION = "0.1.0"