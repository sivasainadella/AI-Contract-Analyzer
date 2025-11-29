from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

from src.ingestion import load_contract
from src.rag_pipeline import RagPipeline
from src.extract_clauses import ClauseExtractor

app = FastAPI(
    title="AI Contract Analyzer",
    description="RAG + NLP pipeline for contract analysis.",
    version="0.1.0",
)

# Initialize core components (in a real system, you'd inject config)
rag_pipeline = RagPipeline()
clause_extractor = ClauseExtractor()


class AnalyzeRequest(BaseModel):
    file_path: str
    question: Optional[str] = None


class AnalyzeResponse(BaseModel):
    summary: str
    clauses: dict
    answer: Optional[str] = None


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_contract(req: AnalyzeRequest):
    """
    Simple endpoint:
    - loads contract
    - indexes it (in-memory)
    - extracts clauses
    - optionally answers a question using RAG
    """
    text = load_contract(req.file_path)
    rag_pipeline.index_text(text)

    clauses = clause_extractor.extract(text)
    summary = rag_pipeline.summarize(text)

    answer = None
    if req.question:
        answer = rag_pipeline.answer_question(req.question)

    return AnalyzeResponse(summary=summary, clauses=clauses, answer=answer)
