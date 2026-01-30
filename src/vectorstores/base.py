from abc import ABC, abstractmethod

class VectorStore(ABC):
    @abstractmethod
    def upsert(self, doc_id: str, text: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(self, query: str, k: int = 3) -> list[str]:
        raise NotImplementedError
