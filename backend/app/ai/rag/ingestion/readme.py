from pathlib import Path

README_NAMES = {
    "readme.md",
    "readme.rst",
    "readme.txt",
}


def is_readme(path: str) -> bool:
    """
    Check whether a file is a README document.

    README filenames are case-insensitive.
    """

    return Path(path).name.lower() in README_NAMES
