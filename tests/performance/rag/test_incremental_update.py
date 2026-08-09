import shutil
import time
from pathlib import Path

from backend.app.ai.rag.incremental.manager import (
    IncrementalManager,
)
from backend.app.ai.rag.incremental.scanner import (
    FileScanner,
)
from backend.app.ai.rag.incremental.tracker import (
    FileTracker,
)


def count_changes(changes):
    result = {}

    for change in changes:
        name = change.change_type.value

        result[name] = result.get(name, 0) + 1

    return result


def copy_dataset(
    source: Path,
    target: Path,
):
    shutil.copytree(
        source,
        target,
    )


def test_incremental_large_update(
    tmp_path,
):
    """
    Large scale incremental update benchmark.

    Flow:

    initial snapshot
        |
        v
    detect changes

        |
        v

    add/update/delete

        |
        v

    incremental index update
    """

    # ------------------------
    # prepare dataset
    # ------------------------

    source = Path(__file__).resolve().parents[2] / "assets" / "rag_large_dataset"

    dataset = tmp_path / "knowledge"

    copy_dataset(
        source,
        dataset,
    )

    tracker = FileTracker(storage_path=str(tmp_path / "tracker.json"))

    scanner = FileScanner(
        root_path=str(dataset),
    )

    manager = IncrementalManager(
        scanner=scanner,
        tracker=tracker,
    )

    # ------------------------
    # first scan
    # ------------------------

    start = time.perf_counter()

    first_changes = manager.update()

    first_time = time.perf_counter() - start

    first_stats = count_changes(first_changes)

    print("\n")
    print("==============================")
    print("Initial Incremental Scan")
    print("==============================")
    print(first_stats)
    print(f"Time: {first_time:.4f}s")

    expected_documents = len([p for p in dataset.rglob("*") if p.is_file()])

    assert first_stats["new"] == expected_documents

    # ------------------------
    # modify dataset
    # ------------------------

    files = list(dataset.rglob("*"))

    files = [f for f in files if f.is_file()]

    # update 50 files

    for file in files[:50]:
        file.write_text(
            file.read_text(encoding="utf-8") + "\nupdated",
            encoding="utf-8",
        )

    # delete 20 files

    for file in files[50:70]:
        file.unlink()

    # add 100 files

    for i in range(100):
        new_file = dataset / "markdown" / f"new_{i}.md"

        new_file.write_text(
            f"""
# New Document {i}

Incremental update test.
""",
            encoding="utf-8",
        )

    # ------------------------
    # second scan
    # ------------------------

    start = time.perf_counter()

    changes = manager.update()

    elapsed = time.perf_counter() - start

    stats = count_changes(changes)

    print("==============================")
    print("Incremental Update Benchmark")
    print("==============================")
    print(stats)
    print(f"Time: {elapsed:.4f}s")

    assert stats["new"] == 100

    assert stats["updated"] == 50

    assert stats["deleted"] == 20
