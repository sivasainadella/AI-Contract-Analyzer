from typing import List, Optional

import faiss
import numpy as np

from .embedding import EmbeddingModel
from .utils import simple_chunk_text


class RagPipeline:
    """
    Very minimal in-memory RAG pipeline.
    - Chunks text
    - Embeds chunks
    - Stores in FAISS index
    - Performs nearest-neighbor search
    - Uses naive summarization (placeholder)
    """

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.index = None
        self.chunks: List[str] = []

    def index_text(self, text: str, chunk_size: int = 800, overlap: int = 100):
        self.chunks = simple_chunk_text(text, chunk_size=chunk_size, overlap=overlap)
        embeddings = self.embedding_model.encode(self.chunks)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings, dtype="float32"))

    def retrieve(self, query: str, k: int = 5) -> List[str]:
        if self.index is None:
            raise ValueError("Index is empty. Call index_text() first.")

        query_vec = self.embedding_model.encode([query]).astype("float32")
        distances, indices = self.index.search(query_vec, k)
        retrieved = [self.chunks[i] for i in indices[0] if i < len(self.chunks)]
        return retrieved

    def summarize(self, text: str) -> str:
        """
        Placeholder summary: first 3–4 sentences.
        In a real implementation, call an LLM here.
        """
        sentences = text.split(".")
        return ". ".join(sentences[:4]).strip() + "."

    def answer_question(self, question: str) -> str:
        """
        Very naive "answer" – concatenate top retrieved chunks.
        In a real system, this would call an LLM with the retrieved context.
        """
        retrieved = self.retrieve(question, k=5)
        context = "\n\n".join(retrieved)
        return f"(Context-based answer placeholder)\n\nCONTEXT:\n{context}"
