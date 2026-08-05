from backend.app.ai.rag.pipeline.batch import (
    batch_split,
)


def test_batch_split():
    items = list(range(10))

    batches = list(
        batch_split(
            items,
            batch_size=3,
        )
    )

    assert batches == [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [9],
    ]


def test_batch_split_empty():
    batches = list(
        batch_split(
            [],
            batch_size=3,
        )
    )

    assert batches == []


def test_batch_split_invalid_size():
    try:
        list(
            batch_split(
                [1, 2, 3],
                batch_size=0,
            )
        )

        assert False

    except ValueError:
        assert True
