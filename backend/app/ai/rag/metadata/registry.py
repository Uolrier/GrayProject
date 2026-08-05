from .manager import MetadataManager


class MetadataRegistry:
    _manager = None

    @classmethod
    def register(cls, manager):
        cls._manager = manager

    @classmethod
    def get(cls):
        if cls._manager is None:
            cls._manager = MetadataManager()

        return cls._manager
