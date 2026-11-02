import unittest
from pathlib import Path
from modules.login_analysis import analyze

ROOT = Path(__file__).resolve().parents[1]

class LoginAnalysisTests(unittest.TestCase):
    def test_counts_and_timeline(self):
        result = analyze(ROOT / "data" / "task_c_signin_logs.csv")
        self.assertEqual(len(result["events"]), 8)
        self.assertEqual(result["counts"]["failed_passwords"], 2)
        self.assertEqual(result["counts"]["mfa_denied"], 1)
        self.assertEqual(result["counts"]["sessions_created"], 1)
        self.assertIn("alone", result["interpretation"])

if __name__ == "__main__":
    unittest.main()
