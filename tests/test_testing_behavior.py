
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "00-python-workflows"
    / "testing_behavior.py"
)

SPEC = importlib.util.spec_from_file_location(
    "testing_behavior",
    MODULE_PATH,
)
testing_behavior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(testing_behavior)


class TestTestingBehavior(unittest.TestCase):
    def test_workflow_returns_summary_after_success(self):
        with patch.object(
            testing_behavior,
            "run_security_check",
            return_value=True,
        ) as mock_check:
            with patch.object(
                testing_behavior,
                "generate_summary",
                return_value="Test summary",
            ) as mock_summary:
                result = testing_behavior.run_workflow()

        self.assertEqual(result, "Test summary")
        mock_check.assert_called_once()
        mock_summary.assert_called_once_with(
            "Analysis complete for: Fix login validation"
        )

    def test_workflow_stops_when_security_check_fails(self):
        with patch.object(
            testing_behavior,
            "run_security_check",
            return_value=False,
        ) as mock_check:
            with patch.object(
                testing_behavior,
                "generate_summary",
            ) as mock_summary:
                result = testing_behavior.run_workflow()

        self.assertIsNone(result)
        mock_check.assert_called_once()
        mock_summary.assert_not_called()


if __name__ == "__main__":
    unittest.main()
