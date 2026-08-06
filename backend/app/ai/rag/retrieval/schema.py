from dataclasses import dataclass
from typing import Dict


@dataclass
class RetrievedDocument:
    """
    Document returned by retriever.
    """

    id: str

    text: str

    score: float

    metadata: Dict
