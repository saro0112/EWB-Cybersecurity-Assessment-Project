import unittest
from pathlib import Path
from modules.account_security import analyze

ROOT = Path(__file__).resolve().parents[1]

class AccountSecurityTests(unittest.TestCase):
    def test_sample_risks_load(self):
        result = analyze(ROOT / "data" / "task_a_risks.json")
        self.assertEqual(result["count"], 5)
        self.assertTrue(result["risks"][0]["control"])

if __name__ == "__main__":
    unittest.main()
