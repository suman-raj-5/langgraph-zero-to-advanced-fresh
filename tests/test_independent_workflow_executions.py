
import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "00-python-workflows"
    / "independent_workflow_executions.py"
)

SPEC = importlib.util.spec_from_file_location(
    "independent_workflow_executions",
    MODULE_PATH,
)
workflow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow)


class TestIndependentWorkflowExecutions(unittest.TestCase):
    def test_each_review_gets_an_independent_findings_list(self):
        review_a = workflow.create_review_state("Authentication fix")
        review_b = workflow.create_review_state("Documentation update")

        self.assertIsNot(
            review_a["findings"],
            review_b["findings"],
        )

    def test_finding_in_one_review_does_not_leak_into_another(self):
        review_a = workflow.run_review(
            "Authentication fix",
            "Hardcoded secret detected",
        )
        review_b = workflow.run_review("Documentation update")

        self.assertEqual(
            review_a["findings"],
            ["Hardcoded secret detected"],
        )
        self.assertEqual(review_b["findings"], [])

    def test_adding_finding_updates_only_the_target_review(self):
        review_a = workflow.create_review_state("Authentication fix")
        review_b = workflow.create_review_state("Documentation update")

        workflow.add_finding(review_a, "Hardcoded secret detected")

        self.assertEqual(
            review_a["status"],
            "analyzed",
        )
        self.assertEqual(
            review_b["status"],
            "started",
        )
        self.assertEqual(review_b["findings"], [])

    def test_each_review_starts_with_its_own_state(self):
        review_a = workflow.run_review("Authentication fix")
        review_b = workflow.run_review("Documentation update")

        self.assertIsNot(review_a, review_b)
        self.assertEqual(review_a["status"], "started")
        self.assertEqual(review_b["status"], "started")


if __name__ == "__main__":
    unittest.main()
