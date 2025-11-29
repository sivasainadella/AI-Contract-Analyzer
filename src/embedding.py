from typing import List

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    SentenceTransformer = None


class EmbeddingModel:
    """
    Simple wrapper around SentenceTransformers.
    Swap this out with any vendor-specific embedding model as needed.
    """

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        if SentenceTransformer is None:
            raise ImportError(
                "sentence-transformers is not installed. "
                "Add it to requirements.txt and pip install."
            )
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: List[str]):
        return self.model.encode(texts, convert_to_numpy=True)
