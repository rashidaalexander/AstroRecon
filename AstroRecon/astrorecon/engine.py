
from __future__ import annotations
import json
from collections import Counter

def load_catalog(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def summarize(path: str) -> dict:
    data = load_catalog(path)["satellites"]
    operators = Counter(item["operator"] for item in data)
    orbits = Counter(item["orbit"] for item in data)
    return {
        "assets": len(data),
        "operators": dict(operators),
        "orbits": dict(orbits),
        "active_assets": [item["name"] for item in data if item["status"] == "active"],
    }
