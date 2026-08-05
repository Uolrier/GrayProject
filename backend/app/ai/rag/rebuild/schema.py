from dataclasses import dataclass


@dataclass
class RebuildRequest:
    """
    Index rebuild request.

    Attributes:
        collection:
            Target vector collection name.

        source_path:
            Source document path used for rebuilding.

        drop_collection:
            Whether to delete the whole collection before rebuilding.
    """

    collection: str
    source_path: str
    drop_collection: bool = False
