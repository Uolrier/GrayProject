"""
项目所有路径统一管理
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BACKEND = ROOT / "backend"

FRONTEND = ROOT / "frontend"

MODELS = ROOT / "models"

DATA = ROOT / "data"

DOCS = ROOT / "docs"

CONFIG = ROOT / "config"

TESTS = ROOT / "tests"
