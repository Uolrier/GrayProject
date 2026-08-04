from app.ai.rag.ingestion.loaders.git import GitLoader


def test_git_loader_local_repository(tmp_path):
    """
    Test loading documents from local repository.
    """

    repo = tmp_path / "demo_repo"
    repo.mkdir()

    # python file
    python_file = repo / "main.py"
    python_file.write_text(
        "print('hello')",
        encoding="utf-8",
    )

    # markdown file
    markdown_file = repo / "README.md"
    markdown_file.write_text(
        "# Demo Project",
        encoding="utf-8",
    )

    loader = GitLoader()

    documents = loader.load(str(repo))

    assert len(documents) == 2

    sources = [doc.metadata["source"] for doc in documents]

    assert str(python_file) in sources
    assert str(markdown_file) in sources


def test_git_loader_ignore_directories(tmp_path):
    """
    Test ignored directories.
    """

    repo = tmp_path / "demo_repo"
    repo.mkdir()

    # normal file
    file = repo / "main.py"
    file.write_text(
        "print('ok')",
        encoding="utf-8",
    )

    # ignored .git file
    git_dir = repo / ".git"
    git_dir.mkdir()

    ignored_file = git_dir / "config"
    ignored_file.write_text(
        "ignore",
        encoding="utf-8",
    )

    loader = GitLoader()

    documents = loader.load(str(repo))

    assert len(documents) == 1

    assert documents[0].metadata["source"] == str(file)


def test_git_loader_unknown_extension(tmp_path):
    """
    Test unsupported files are skipped.
    """

    repo = tmp_path / "demo_repo"
    repo.mkdir()

    unknown = repo / "data.xyz"
    unknown.write_text(
        "unknown",
        encoding="utf-8",
    )

    loader = GitLoader()

    documents = loader.load(str(repo))

    assert documents == []
