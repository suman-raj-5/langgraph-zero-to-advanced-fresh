
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "00-python-workflows"
    / "reusable_steps.py"
)

SPEC = importlib.util.spec_from_file_location(
    "reusable_steps",
    MODULE_PATH,
)
reusable_steps = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reusable_steps)


class TestReusableSteps(unittest.TestCase):
    def test_collect_pr_details(self):
        details = reusable_steps.collect_pr_details()

        self.assertEqual(details["title"], "Fix login validation")
        self.assertEqual(
            details["description"],
            "Validate user input before login",
        )

    def test_analyze_pr(self):
        details = {
            "title": "Fix login validation",
            "description": "Validate user input before login",
        }

        analysis = reusable_steps.analyze_pr(details)

        self.assertEqual(analysis["title"], "Fix login validation")
        self.assertEqual(analysis["assessment"], "Sufficient description")

    def test_analyze_pr_with_short_description(self):
        details = {
            "title": "Fix login validation",
            "description": "Fix bug",
        }

        analysis = reusable_steps.analyze_pr(details)

        self.assertEqual(
            analysis["assessment"],
            "Description needs more detail",
        )

    def test_generate_summary(self):
        analysis = {
            "title": "Fix login validation",
            "assessment": "Sufficient description",
        }

        summary = reusable_steps.generate_summary(analysis)

        self.assertEqual(
            summary,
            "PR Review: Fix login validation - Sufficient description",
        )

    def test_run_workflow(self):
        summary = reusable_steps.run_workflow()

        self.assertEqual(
            summary,
            "PR Review: Fix login validation - Sufficient description",
        )

    def test_run_workflow_calls_steps_in_order(self):
        with (
            patch.object(
                reusable_steps,
                "collect_pr_details",
                return_value={"title": "Example", "description": "Example details"},
            ) as collect,
            patch.object(
                reusable_steps,
                "analyze_pr",
                return_value={"title": "Example", "assessment": "Passed"},
            ) as analyze,
            patch.object(
                reusable_steps,
                "generate_summary",
                return_value="Example summary",
            ) as generate,
        ):
            result = reusable_steps.run_workflow()

        self.assertEqual(result, "Example summary")
        collect.assert_called_once_with()
        analyze.assert_called_once_with(
            {"title": "Example", "description": "Example details"}
        )
        generate.assert_called_once_with(
            {"title": "Example", "assessment": "Passed"}
        )


if __name__ == "__main__":
    unittest.main()
