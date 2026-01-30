from abc import ABC, abstractmethod

class WebSearchProvider(ABC):
    @abstractmethod
    def search(self, query: str) -> list[str]:
        raise NotImplementedError
