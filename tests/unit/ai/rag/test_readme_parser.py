from backend.app.ai.rag.ingestion.readme import is_readme


def test_readme_detection():
    assert is_readme("README.md")

    assert is_readme("README.MD")

    assert is_readme("readme.md")

    assert is_readme("README.rst")

    assert is_readme("README.txt")


def test_non_readme_detection():
    assert not is_readme("main.md")

    assert not is_readme("notes.txt")


def test_readme_case_insensitive():
    assert is_readme("README.md")

    assert is_readme("ReadMe.md")

    assert is_readme("readme.MD")

    assert is_readme("README.RST")
