from typing import List

from .schema import SourceReference


class SourceBuilder:
    """
    Build source references from retrieved documents.
    """

    def build(
        self,
        documents,
    ) -> List[SourceReference]:
        sources = []

        for doc in documents:
            metadata = (
                getattr(
                    doc,
                    "metadata",
                    {},
                )
                or {}
            )

            sources.append(
                SourceReference(
                    file_path=metadata.get(
                        "source",
                        "",
                    ),
                    chunk_id=str(
                        metadata.get(
                            "chunk_id",
                            "",
                        )
                    ),
                    score=float(
                        getattr(
                            doc,
                            "score",
                            0,
                        )
                    ),
                    page=metadata.get(
                        "page",
                    ),
                    line_start=metadata.get(
                        "line_start",
                    ),
                    line_end=metadata.get(
                        "line_end",
                    ),
                )
            )

        return sources
