
import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "00-python-workflows"
    / "validation_and_contracts.py"
)

SPEC = importlib.util.spec_from_file_location(
    "validation_and_contracts",
    MODULE_PATH,
)
validation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validation)


class TestValidationAndContracts(unittest.TestCase):
    def test_valid_pr_details_are_accepted(self):
        details = {
            "title": "Fix login validation",
            "description": "Validate user input before login",
        }

        result = validation.validate_pr_details(details)

        self.assertIs(result, details)

    def test_non_dictionary_input_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError, "PR details must be a dictionary"
        ):
            validation.validate_pr_details(None)

    def test_missing_title_is_rejected(self):
        details = {
            "description": "Validate user input before login",
        }

        with self.assertRaisesRegex(
            ValueError, "PR title must be a non-empty string"
        ):
            validation.validate_pr_details(details)

    def test_empty_title_is_rejected(self):
        details = {
            "title": "   ",
            "description": "Validate user input before login",
        }

        with self.assertRaisesRegex(
            ValueError, "PR title must be a non-empty string"
        ):
            validation.validate_pr_details(details)

    def test_non_string_description_is_rejected(self):
        details = {
            "title": "Fix login validation",
            "description": None,
        }

        with self.assertRaisesRegex(
            ValueError, "PR description must be a non-empty string"
        ):
            validation.validate_pr_details(details)

    def test_whitespace_description_is_rejected(self):
        details = {
            "title": "Fix login validation",
            "description": "   ",
        }

        with self.assertRaisesRegex(
            ValueError, "PR description must be a non-empty string"
        ):
            validation.validate_pr_details(details)

    def test_analysis_validates_before_processing(self):
        details = {
            "title": "Fix login validation",
            "description": None,
        }

        with self.assertRaisesRegex(
            ValueError, "PR description must be a non-empty string"
        ):
            validation.analyze_pr(details)

    def test_valid_input_produces_assessment(self):
        details = {
            "title": "Fix login validation",
            "description": "Validate user input before login",
        }

        result = validation.analyze_pr(details)

        self.assertEqual(result["title"], "Fix login validation")
        self.assertEqual(result["assessment"], "Sufficient description")


if __name__ == "__main__":
    unittest.main()
