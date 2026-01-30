import os
import sys

def fail(msg: str):
    print(f"[FAIL] {msg}")
    sys.exit(1)

def warn(msg: str):
    print(f"[WARN] {msg}")

def ok(msg: str):
    print(f"[OK] {msg}")

def main():
    if not os.path.exists(".env"):
        fail(".env file is missing")

    env = open(".env", "r", encoding="utf-8").read()

    if "RAG_API_KEY=" not in env:
        fail("RAG_API_KEY is missing")

    if "RAG_API_KEY=change-me" in env:
        fail("RAG_API_KEY still set to placeholder")

    ok("API key configured")

    if "WEB_SEARCH_ENABLED=true" in env:
        warn("Web search is ENABLED  ensure this is intentional")

    ok("Audit completed")

if __name__ == "__main__":
    main()
