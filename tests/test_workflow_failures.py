
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "00-python-workflows"
    / "workflow_failures.py"
)

SPEC = importlib.util.spec_from_file_location(
    "workflow_failures",
    MODULE_PATH,
)
workflow_failures = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow_failures)


class TestWorkflowFailures(unittest.TestCase):
    def setUp(self):
        workflow_failures.security_check_attempts = 0

    def test_security_check_fails_first_then_succeeds(self):
        with self.assertRaises(RuntimeError):
            workflow_failures.run_security_check()

        self.assertEqual(workflow_failures.security_check_attempts, 1)

        workflow_failures.run_security_check()
        self.assertEqual(workflow_failures.security_check_attempts, 2)

    def test_workflow_retries_after_failure(self):
        with patch.object(
            workflow_failures,
            "run_security_check",
            side_effect=[
                RuntimeError("Temporary failure"),
                None,
            ],
        ) as mock_check:
            with patch.object(
                workflow_failures,
                "generate_summary",
                return_value="Test summary",
            ) as mock_summary:
                workflow_failures.run_workflow()

        self.assertEqual(mock_check.call_count, 2)
        mock_summary.assert_called_once()

    def test_workflow_stops_after_two_failures(self):
        with patch.object(
            workflow_failures,
            "run_security_check",
            side_effect=RuntimeError("Persistent failure"),
        ) as mock_check:
            with patch.object(
                workflow_failures,
                "generate_summary",
            ) as mock_summary:
                workflow_failures.run_workflow()

        self.assertEqual(mock_check.call_count, 2)
        mock_summary.assert_not_called()


if __name__ == "__main__":
    unittest.main()
