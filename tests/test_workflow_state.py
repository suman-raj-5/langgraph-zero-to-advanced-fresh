
import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "00-python-workflows"
    / "workflow_state.py"
)

SPEC = importlib.util.spec_from_file_location(
    "workflow_state",
    MODULE_PATH,
)
workflow_state = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow_state)


class TestWorkflowState(unittest.TestCase):
    def test_create_initial_state(self):
        state = workflow_state.create_initial_state()

        self.assertEqual(state["title"], "Fix login validation")
        self.assertEqual(
            state["description"],
            "Validate user input before login",
        )
        self.assertEqual(state["status"], "started")
        self.assertNotIn("assessment", state)
        self.assertNotIn("summary", state)

    def test_analyze_state_updates_existing_state(self):
        state = workflow_state.create_initial_state()
        result = workflow_state.analyze_state(state)

        self.assertIs(result, state)
        self.assertEqual(
            state["assessment"],
            "Sufficient description",
        )
        self.assertEqual(state["status"], "analyzed")
        self.assertEqual(state["title"], "Fix login validation")

    def test_analyze_state_with_short_description(self):
        state = {
            "title": "Fix login validation",
            "description": "Fix bug",
            "status": "started",
        }

        workflow_state.analyze_state(state)

        self.assertEqual(
            state["assessment"],
            "Description needs more detail",
        )

    def test_generate_summary_updates_existing_state(self):
        state = workflow_state.create_initial_state()
        workflow_state.analyze_state(state)
        result = workflow_state.generate_summary_state(state)

        self.assertIs(result, state)
        self.assertEqual(
            state["summary"],
            "PR Review: Fix login validation - Sufficient description",
        )
        self.assertEqual(state["status"], "completed")
        self.assertIn("description", state)

    def test_run_workflow(self):
        state = workflow_state.run_workflow()

        self.assertEqual(state["status"], "completed")
        self.assertEqual(
            state["assessment"],
            "Sufficient description",
        )
        self.assertEqual(
            state["summary"],
            "PR Review: Fix login validation - Sufficient description",
        )


if __name__ == "__main__":
    unittest.main()
