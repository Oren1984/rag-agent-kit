from abc import ABC, abstractmethod

class AppConnector(ABC):
    @abstractmethod
    def fetch_context(self, question: str) -> str:
        raise NotImplementedError
