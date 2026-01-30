import json
import subprocess
from datetime import datetime

def get_git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        return "unknown"

def build_info() -> dict:
    return {
        "version": "0.1.0",
        "commit": get_git_commit(),
        "build_time": datetime.utcnow().isoformat() + "Z"
    }

def write_build_info(path: str = "BUILD_INFO.json") -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(build_info(), f, indent=2)
