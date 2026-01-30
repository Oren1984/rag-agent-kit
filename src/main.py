# src/main.py
# Main application entry point for the RAG Agent Kit application.

from fastapi import FastAPI
from src.core.settings import settings
from src.api.routes import router
from src.meta.build_info import build_info
from src.middleware.rate_limit import rate_limit_middleware
from src.middleware.security_headers import security_headers_middleware
from src.middleware.cors import cors_middleware

# Create and configure the FastAPI application
def create_app() -> FastAPI:
    if not settings.rag_api_key or settings.rag_api_key.strip() == "":
        raise RuntimeError("RAG_API_KEY is required. Set it in .env (or environment).")

    app = FastAPI(title=settings.app_name)
    app.state.build = build_info()

    # Middlewares (safe defaults)
    cors_middleware(app)               # locked unless enabled + origins provided
    security_headers_middleware(app)
    rate_limit_middleware(app)

    app.include_router(router)
    return app

app = create_app()
