"""Task D: Review fictional AI-generated cybersecurity claims."""
import json
from pathlib import Path

def load_claims(path):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"AI claims file not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError("Task D data must be a JSON list.")
    required = {"claim", "problem", "correction", "recommendation"}
    for index, item in enumerate(data, 1):
        if not isinstance(item, dict) or not required.issubset(item):
            raise ValueError(f"Task D claim {index} is missing required fields.")
    return data

def analyze(path):
    claims = load_claims(path)
    return {"title": "Task D - AI Security Advice Evaluation", "count": len(claims), "claims": claims}
