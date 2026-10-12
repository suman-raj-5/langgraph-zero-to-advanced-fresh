
import importlib.util
import unittest
from pathlib import Path


# Load the lesson file for testing.
lesson_path = (
    Path(__file__).resolve().parent.parent
    / "00-python-workflows"
    / "sequential_workflow.py"
)

spec = importlib.util.spec_from_file_location(
    "sequential_workflow", lesson_path
)
workflow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workflow)


class TestSequentialWorkflow(unittest.TestCase):

    def test_collect_pr_details(self):
        title, description = workflow.collect_pr_details()

        self.assertEqual(title, "Fix login validation")
        self.assertTrue(len(description) > 0)

    def test_analyze_pr_with_enough_detail(self):
        description = (
            "Validate empty usernames and reject invalid login requests."
        )

        result = workflow.analyze_pr(description)

        self.assertEqual(
            result,
            "The PR description has enough detail.",
        )

    def test_analyze_pr_with_short_description(self):
        result = workflow.analyze_pr("Fix bug")

        self.assertEqual(
            result,
            "The PR description needs more detail.",
        )

    def test_run_workflow(self):
        result = workflow.run_workflow()

        self.assertIn("Fix login validation", result)
        self.assertIn(
            "The PR description has enough detail.",
            result,
        )


if __name__ == "__main__":
    unittest.main()
