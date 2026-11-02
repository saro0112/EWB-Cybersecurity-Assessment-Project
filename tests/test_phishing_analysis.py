import unittest
from pathlib import Path
from modules.phishing_analysis import analyze

ROOT = Path(__file__).resolve().parents[1]

class PhishingTests(unittest.TestCase):
    def test_sample_email_loads(self):
        result = analyze(ROOT / "data" / "task_b_email.json")
        self.assertGreaterEqual(result["warning_sign_count"], 5)
        self.assertIn("HTTPS", " ".join(result["email"]["verification_steps"]))

if __name__ == "__main__":
    unittest.main()
