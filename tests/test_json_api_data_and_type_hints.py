import importlib.util
import json
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "00-python-workflows"
    / "json_api_data_and_type_hints.py"
)

SPEC = importlib.util.spec_from_file_location(
    "json_api_data_and_type_hints",
    MODULE_PATH,
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

parse_pr_payload = MODULE.parse_pr_payload
serialize_pr_payload = MODULE.serialize_pr_payload


class TestJsonApiDataAndTypeHints(unittest.TestCase):
    def setUp(self):
        self.payload = json.dumps(
            {
                "number": 42,
                "title": "  Fix login validation  ",
                "changed_files": 3,
            }
        )

    def test_parse_valid_payload(self):
        result = parse_pr_payload(self.payload)

        self.assertEqual(
            result,
            {
                "number": 42,
                "title": "Fix login validation",
                "changed_files": 3,
            },
        )

    def test_serialize_payload(self):
        data = parse_pr_payload(self.payload)

        serialized = serialize_pr_payload(data)

        self.assertEqual(json.loads(serialized), data)

    def test_invalid_json_raises_value_error(self):
        with self.assertRaisesRegex(
            ValueError, "Payload must contain valid JSON"
        ):
            parse_pr_payload("{invalid json")

    def test_non_object_json_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError, "PR payload must be a JSON object"
        ):
            parse_pr_payload("[1, 2, 3]")

    def test_missing_number_is_rejected(self):
        payload = json.dumps(
            {"title": "Fix login validation", "changed_files": 3}
        )

        with self.assertRaisesRegex(ValueError, "PR number"):
            parse_pr_payload(payload)

    def test_boolean_number_is_rejected(self):
        payload = json.dumps(
            {"number": True, "title": "Fix login validation",
             "changed_files": 3}
        )

        with self.assertRaisesRegex(ValueError, "PR number"):
            parse_pr_payload(payload)

    def test_blank_title_is_rejected(self):
        payload = json.dumps(
            {"number": 42, "title": "   ", "changed_files": 3}
        )

        with self.assertRaisesRegex(ValueError, "PR title"):
            parse_pr_payload(payload)

    def test_negative_changed_files_is_rejected(self):
        payload = json.dumps(
            {"number": 42, "title": "Fix login validation",
             "changed_files": -1}
        )

        with self.assertRaisesRegex(ValueError, "changed_files"):
            parse_pr_payload(payload)


if __name__ == "__main__":
    unittest.main()