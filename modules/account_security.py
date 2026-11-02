"""Task A: Analyze fictional student account security risks."""
import json
from pathlib import Path

def load_risks(path):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Risk data file not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError("Task A data must be a JSON list.")
    required = {"risk", "asset", "confidentiality", "integrity", "availability", "control", "limitation"}
    for index, item in enumerate(data, 1):
        if not isinstance(item, dict) or not required.issubset(item):
            raise ValueError(f"Task A item {index} is missing required fields.")
    return data

def analyze(path):
    risks = load_risks(path)
    return {"title": "Task A - Account Security Risk Analysis", "count": len(risks), "risks": risks}
