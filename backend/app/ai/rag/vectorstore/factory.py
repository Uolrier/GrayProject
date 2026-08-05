from .chroma import ChromaVectorStore


class VectorStoreFactory:
    @staticmethod
    def create(name="chroma", **kwargs):
        if name == "chroma":
            return ChromaVectorStore(**kwargs)

        raise ValueError(f"Unknown vector store: {name}")
