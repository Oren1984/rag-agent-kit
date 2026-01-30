from pathlib import Path
from src.connectors.base import AppConnector

class FilesConnector(AppConnector):
    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)

    def fetch_context(self, question: str) -> str:
        if not self.base_path.exists():
            return "No files directory found."

        texts = []
        for p in self.base_path.glob("**/*.txt"):
            try:
                texts.append(p.read_text(encoding="utf-8")[:2000])
            except Exception:
                continue

        if not texts:
            return "No readable files found."

        return "\n---\n".join(texts[:3])
