import unittest
from pathlib import Path
from modules.ai_advice_review import analyze

ROOT = Path(__file__).resolve().parents[1]

class AIAdviceTests(unittest.TestCase):
    def test_five_claims_load(self):
        result = analyze(ROOT / "data" / "task_d_ai_claims.json")
        self.assertEqual(result["count"], 5)
        self.assertTrue(all(item["recommendation"] for item in result["claims"]))

if __name__ == "__main__":
    unittest.main()
