import os
import time
import requests

BASE = "http://127.0.0.1:8000"

def load_api_key() -> str:
    if not os.path.exists(".env"):
        raise SystemExit("Missing .env")
    for line in open(".env", "r", encoding="utf-8"):
        if line.startswith("RAG_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("Missing RAG_API_KEY in .env")

def main():
    key = load_api_key()

    # health
    h = requests.get(f"{BASE}/health", timeout=5).json()
    print("health:", h)

    # ready
    r = requests.get(f"{BASE}/ready", timeout=5).json()
    print("ready:", r)

    # ask (authorized)
    headers = {"X-API-Key": key}
    payload = {"question": "What is this service?"}
    a = requests.post(f"{BASE}/ask", json=payload, headers=headers, timeout=10).json()
    print("ask:", a)

    # ask (unauthorized should fail)
    bad = requests.post(f"{BASE}/ask", json=payload, timeout=10)
    if bad.status_code != 401:
        raise SystemExit(f"Expected 401, got {bad.status_code}")
    print("unauthorized: OK")

    print("SMOKE TEST PASSED")

if __name__ == "__main__":
    main()
