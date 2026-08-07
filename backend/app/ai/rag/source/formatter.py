from typing import List

from .schema import SourceReference


class SourceFormatter:
    """
    Format source references for display/logging.
    """

    def format(
        self,
        sources: List[SourceReference],
    ) -> str:
        lines = []

        for index, source in enumerate(
            sources,
            start=1,
        ):
            lines.append((f"[{index}] {source.file_path} (score={source.score:.3f})"))

        return "\n".join(lines)
