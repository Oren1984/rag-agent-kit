from abc import ABC, abstractmethod

class Embeddings(ABC):
    @abstractmethod
    def embed(self, text: str) -> list[float]:
        raise NotImplementedError
