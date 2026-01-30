from src.core.settings import settings

from src.providers.openai_provider import OpenAIProvider
from src.providers.gemini_provider import GeminiProvider
from src.providers.anthropic_provider import AnthropicProvider

from src.connectors.rest_connector import RestConnector
from src.connectors.files.files_connector import FilesConnector

from src.vectorstores.memory_store import MemoryVectorStore
from src.vectorstores.pgvector_store import PGVectorStore

from src.websearch.tavily_search import TavilySearch
from src.websearch.serper_search import SerperSearch

_store = None

def _get_provider():
    p = settings.llm_provider.lower().strip()
    if p == "gemini":
        return GeminiProvider()
    if p == "anthropic":
        return AnthropicProvider()
    return OpenAIProvider()

def _get_connector():
    c = settings.connector.lower().strip()
    if c == "files":
        return FilesConnector(settings.files_base_path)
    return RestConnector()

def _get_web_search():
    p = settings.web_search_provider.lower().strip()
    if p == "serper":
        return SerperSearch()
    return TavilySearch()

def _get_store():
    global _store
    if _store is not None:
        return _store

    vs = settings.vectorstore.lower().strip()
    if vs == "pgvector":
        # Fail-fast requirement: embeddings need OPENAI_API_KEY
        if not settings.openai_api_key:
            raise RuntimeError("VECTORSTORE=pgvector requires OPENAI_API_KEY for embeddings")
        _store = PGVectorStore()
    else:
        _store = MemoryVectorStore()

    # bootstrap
    _store.upsert("boot", "This is a default knowledge snippet (boot).")
    return _store

def answer_question(question: str) -> dict:
    connector = _get_connector()
    provider = _get_provider()
    web = _get_web_search()
    store = _get_store()

    app_ctx = connector.fetch_context(question)
    retrieved = store.search(question, k=3)
    web_results = web.search(question) if settings.web_search_enabled else []

    prompt = (
        "You are a RAG agent. Answer using the provided context.\n\n"
        f"APP_CONTEXT:\n{app_ctx}\n\n"
        f"RETRIEVED:\n- " + "\n- ".join(retrieved) + "\n\n"
        + (f"WEB_RESULTS:\n- " + "\n- ".join(web_results) + "\n\n" if web_results else "")
        + f"QUESTION:\n{question}\n"
    )

    answer = provider.generate(prompt)

    return {
        "answer": answer,
        "provider": settings.llm_provider,
        "connector": settings.connector,
        "vectorstore": settings.vectorstore,
        "web_search_enabled": settings.web_search_enabled,
        "sources": {
            "app_context": app_ctx,
            "retrieved_count": len(retrieved),
            "web_results_count": len(web_results),
        },
    }
