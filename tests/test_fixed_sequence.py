
import importlib.util
import unittest
from pathlib import Path


lesson_path = (
    Path(__file__).resolve().parent.parent
    / "00-python-workflows"
    / "fixed_sequence.py"
)

spec = importlib.util.spec_from_file_location(
    "fixed_sequence", lesson_path
)
workflow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workflow)


class TestReviewDecision(unittest.TestCase):

    def test_security_issue_selects_warning(self):
        analysis = "Security issue found in login"

        action = workflow.choose_review_action(analysis)

        self.assertEqual(action, "security_warning")

    def test_normal_analysis_selects_summary(self):
        analysis = "Analysis complete for login"

        action = workflow.choose_review_action(analysis)

        self.assertEqual(action, "normal_summary")


if __name__ == "__main__":
    unittest.main()
