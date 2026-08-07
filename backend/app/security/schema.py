from dataclasses import dataclass, field


@dataclass
class SecurityResult:
    """
    Security check result.
    """

    passed: bool

    score: float = 0.0

    matched_rules: list[str] = field(default_factory=list)

    reason: str | None = None
