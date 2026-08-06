from .registry import get_vectorstore


class VectorStoreFactory:
    @staticmethod
    def create(
        name="chroma",
        **kwargs,
    ):
        store_cls = get_vectorstore(name)

        return store_cls(**kwargs)
