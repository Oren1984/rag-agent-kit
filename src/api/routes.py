# src/api/routes.py
# API route definitions for the RAG Agent Kit application.

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from src.security.auth import require_api_key
from src.core.settings import settings
from src.retrieval.pipeline import answer_question

router = APIRouter()

# Pydantic model for the ask request payload
class AskRequest(BaseModel):
    question: str

# Health check endpoint
@router.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}

# Readiness check endpoint
@router.get("/ready")
def ready():
    # minimal readiness checks
    ok = bool(settings.rag_api_key and settings.rag_api_key.strip())
    return {"ready": ok, "provider": settings.llm_provider}

# Endpoint to handle question answering
@router.post("/ask")
def ask(payload: AskRequest, _=Depends(require_api_key)):
    return answer_question(payload.question)
