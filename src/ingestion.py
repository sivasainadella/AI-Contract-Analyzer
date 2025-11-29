import pdfplumber
from pathlib import Path


def load_contract(file_path: str) -> str:
    """
    Load contract text from a PDF file.
    For DOCX or other formats, extend this function.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() == ".pdf":
        return _load_pdf(path)
    else:
        # simple fallback: treat as plain text
        return path.read_text(encoding="utf-8")


def _load_pdf(path: Path) -> str:
    text_chunks = []
    with pdfplumber.open(str(path)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text_chunks.append(page_text)
    return "\n".join(text_chunks)
