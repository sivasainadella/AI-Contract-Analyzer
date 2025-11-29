# AI-Contract-Analyzer
This project is an end-to-end NLP pipeline to analyze contracts using
LLMs, vector search, and retrieval-augmented generation (RAG). It is
designed for real-world contracting complexity, especially in
biotech/pharma, payer–provider agreements, and B2B enterprise deals.

The goal is to turn unstructured contract language into structured,
searchable, and actionable insights for **revenue, compliance, and legal
teams**.

## Key Features
- 🔍 Clause extraction (pricing, rebates, SLAs, termination, audit, data protection)
- 🧠 RAG-based semantic search over contract text
- 📄 Document ingestion & chunking pipeline
- 🧱 Pluggable embedding layer (HuggingFace, OpenAI, etc.)
- 🔌 Simple FastAPI layer for integration with CLM/CRM/revenue systems

## 🧠 High-Level Architecture

1. **Ingestion** – Load PDF/DOCX → extract raw text  
2. **Chunking** – Split text into semantically meaningful segments  
3. **Embeddings** – Convert chunks to vectors  
4. **Vector Store** – Index and search similar chunks  
5. **RAG Pipeline** – Retrieve chunks + generate answer/summary  
6. **Clause Layer** – Extract specific clauses (rebate, pricing, SLA, etc.)

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **Frameworks:** FastAPI, Uvicorn
- **NLP/Vector:** SentenceTransformers / HuggingFace, FAISS (or similar)
- **Parsing:** pdfplumber / PyPDF2 (pluggable)

This repo intentionally keeps the implementation **modular and vendor-neutral** so it can be wired to any LLM / embedding provider.

## 🚀 Quickstart

```bash
# create and activate virtual env (optional but recommended)
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run the API
uvicorn app:app --reload


