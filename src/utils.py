from typing import List


def simple_chunk_text(text: str, chunk_size: int = 800, overlap: int = 100) -> List[str]:
    """
    Naive character-based chunking with overlap.
    This can be replaced later with token-based or semantic chunking.
    """
    chunks = []
    start = 0
    length = len(text)

    while start < length:
        end = min(start + chunk_size, length)
        chunk = text[start:end]
        chunks.append(chunk)
        if end == length:
            break
        start = end - overlap

    return chunks
