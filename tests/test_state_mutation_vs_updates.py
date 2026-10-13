
import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "00-python-workflows"
    / "state_mutation_vs_updates.py"
)

SPEC = importlib.util.spec_from_file_location(
    "state_mutation_vs_updates",
    MODULE_PATH,
)
state_workflow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(state_workflow)


class TestStateMutationVsUpdates(unittest.TestCase):
    def test_mutation_changes_original_state(self):
        state = state_workflow.create_initial_state()

        result = state_workflow.analyze_with_mutation(state)

        self.assertIs(result, state)
        self.assertEqual(state["status"], "analyzed")
        self.assertIn("assessment", state)

    def test_updates_leave_original_state_unchanged(self):
        state = state_workflow.create_initial_state()
        original_state = state.copy()

        update = state_workflow.analyze_with_updates(state)

        self.assertEqual(state, original_state)
        self.assertEqual(update["status"], "analyzed")
        self.assertIn("assessment", update)

    def test_applying_updates_changes_state(self):
        state = state_workflow.create_initial_state()

        update = state_workflow.analyze_with_updates(state)
        state.update(update)

        self.assertEqual(state["status"], "analyzed")
        self.assertIn("assessment", state)
        self.assertEqual(state["title"], "Fix authentication")

    def test_both_workflows_produce_equivalent_results(self):
        mutation_result = state_workflow.run_mutation_workflow()
        update_result = state_workflow.run_update_workflow()

        self.assertEqual(mutation_result, update_result)


if __name__ == "__main__":
    unittest.main()
