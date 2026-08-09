#!/usr/bin/env python3
"""
输出项目目录树到 project_tree.txt

用法：
    python tree.py
    python tree.py /path/to/project
"""

import sys
from pathlib import Path

# 忽略的目录
IGNORE_DIRS = {
    ".git",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "dist",
    "build",
    "data",
    ".DS_Store",
    "project_tree.txt",
    # large test datasets
    "rag_large_dataset",
}

# 忽略的文件
IGNORE_FILES = {
    ".DS_Store",
}

OUTPUT_FILE = "project_tree.txt"


def should_ignore(path: Path) -> bool:
    return path.name in IGNORE_DIRS or path.name in IGNORE_FILES


def build_tree(path: Path, prefix: str = "", lines=None):
    if lines is None:
        lines = []

    entries = sorted(
        [p for p in path.iterdir() if not should_ignore(p)],
        key=lambda p: (p.is_file(), p.name.lower()),
    )

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "

        line = prefix + connector + entry.name
        lines.append(line)

        if entry.is_dir():
            extension = "    " if is_last else "│   "
            build_tree(entry, prefix + extension, lines)

    return lines


def main():
    if len(sys.argv) > 1:
        root = Path(sys.argv[1]).resolve()
    else:
        root = Path.cwd()

    if not root.exists():
        print(f"路径不存在：{root}")
        return

    lines = [root.name]
    build_tree(root, lines=lines)

    output_path = root / OUTPUT_FILE

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("\n".join(lines))
    print(f"\n项目树已保存到：{output_path}")


if __name__ == "__main__":
    main()
