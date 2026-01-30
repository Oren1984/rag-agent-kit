from src.vectorstores.base import VectorStore

class MemoryVectorStore(VectorStore):
    def __init__(self) -> None:
        self._docs: dict[str, str] = {}

    def upsert(self, doc_id: str, text: str) -> None:
        self._docs[doc_id] = text

    def search(self, query: str, k: int = 3) -> list[str]:
        # naive: return up to k docs
        return list(self._docs.values())[:k]
