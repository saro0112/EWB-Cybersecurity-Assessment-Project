"""Task B: Analyze a fictional scholarship email for phishing indicators."""
import json
from pathlib import Path

def load_email(path):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Email data file not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    required = {"sender", "reply_to", "subject", "requests", "warning_signs", "verification_steps"}
    if not isinstance(data, dict) or not required.issubset(data):
        raise ValueError("Task B email data is missing required fields.")
    return data

def analyze(path):
    email = load_email(path)
    return {"title": "Task B - Phishing Email Analysis", "email": email,
            "warning_sign_count": len(email["warning_signs"])}
