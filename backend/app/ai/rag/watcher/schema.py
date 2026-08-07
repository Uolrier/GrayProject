from dataclasses import dataclass


@dataclass
class WatcherConfig:
    path: str
    interval: int = 30
    enabled: bool = True
