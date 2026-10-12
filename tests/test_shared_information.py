
import importlib.util
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO


lesson_path = (
    Path(__file__).resolve().parent.parent
    / "00-python-workflows"
    / "shared_information.py"
)

spec = importlib.util.spec_from_file_location(
    "shared_information", lesson_path
)
workflow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workflow)


class TestSharedInformation(unittest.TestCase):

    def test_collect_pr_details_returns_dictionary(self):
        pr_details = workflow.collect_pr_details()

        self.assertIsInstance(pr_details, dict)
        self.assertEqual(pr_details["title"], "Fix login validation")
        self.assertEqual(pr_details["test_status"], "passed")

    def test_summary_uses_shared_information(self):
        pr_details = workflow.collect_pr_details()
        output = StringIO()

        with redirect_stdout(output):
            workflow.generate_summary(pr_details)

        summary = output.getvalue()

        self.assertIn("Fix login validation", summary)
        self.assertIn("auth.py, login.py", summary)
        self.assertIn("Tests: passed", summary)
        self.assertIn("SQL injection risk", summary)

    def test_run_workflow(self):
        output = StringIO()

        with redirect_stdout(output):
            workflow.run_workflow()

        self.assertIn("Review", output.getvalue()) if "Review" in output.getvalue() else self.assertIn("PR:", output.getvalue())


if __name__ == "__main__":
    unittest.main()
