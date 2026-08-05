import hashlib


def create_embedding_cache_key(
    text: str,
    model: str,
) -> str:
    """
    Create stable cache key for embedding.

    Same text with different models
    should generate different keys.
    """

    content = f"{model}:{text}"

    return hashlib.sha256(content.encode("utf-8")).hexdigest()
