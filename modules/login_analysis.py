"""Task C: Analyze synthetic login events. This module does not inspect live systems."""
import csv
from pathlib import Path

REQUIRED_COLUMNS = {"timestamp", "event_type", "status", "ip_address", "mfa_status", "session"}

def load_events(path):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Login CSV file not found: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("Login CSV is empty or has no header.")
        missing = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing:
            raise ValueError("Login CSV is missing columns: " + ", ".join(sorted(missing)))
        rows = list(reader)
    if not rows:
        raise ValueError("Login CSV contains no event records.")
    return sorted(rows, key=lambda row: row["timestamp"])

def analyze(path):
    events = load_events(path)
    counts = {
        "failed_passwords": sum(e["event_type"] == "password" and e["status"] == "failed" for e in events),
        "successful_passwords": sum(e["event_type"] == "password" and e["status"] == "success" for e in events),
        "mfa_denied": sum(e["event_type"] == "mfa" and e["mfa_status"] == "denied" for e in events),
        "mfa_approved": sum(e["event_type"] == "mfa" and e["mfa_status"] == "approved" for e in events),
        "sessions_created": sum(e["event_type"] == "session" for e in events),
    }
    return {"title": "Task C - Login Activity Analysis", "events": events, "counts": counts,
            "interpretation": "The sequence deserves review, but an IP address difference alone does not prove an attacker.",
            "checks": ["Ask the account owner to confirm the activity through a trusted channel.",
                       "Have authorised IT staff review identity-provider sign-in details and preserve relevant logs."]}
