import sys
from pathlib import Path

# 添加项目根目录到 Python 路径

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))


import uvicorn  # noqa: E402

if __name__ == "__main__":

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
