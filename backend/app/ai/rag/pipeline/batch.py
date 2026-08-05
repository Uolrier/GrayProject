def batch_split(
    items,
    batch_size: int,
):
    """
    Split items into batches.

    Args:
        items:
            input list

        batch_size:
            max items per batch
    """

    if batch_size <= 0:
        raise ValueError("batch_size must be greater than zero")

    for index in range(
        0,
        len(items),
        batch_size,
    ):
        yield items[index : index + batch_size]
