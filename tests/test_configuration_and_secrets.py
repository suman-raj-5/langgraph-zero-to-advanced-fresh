
import importlib.util
import os
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "00-python-workflows"
    / "configuration_and_secrets.py"
)

SPEC = importlib.util.spec_from_file_location(
    "configuration_and_secrets",
    MODULE_PATH,
)
config_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(config_module)


class TestLoadConfig(unittest.TestCase):
    def test_loads_valid_configuration(self):
        with patch.dict(
            os.environ,
            {"MODEL_NAME": "demo-model", "MAX_RETRIES": "3"},
            clear=True,
        ):
            config = config_module.load_config()

        self.assertEqual(config["model_name"], "demo-model")
        self.assertEqual(config["max_retries"], 3)
        self.assertIsInstance(config["max_retries"], int)

    def test_uses_default_retry_count(self):
        with patch.dict(
            os.environ,
            {"MODEL_NAME": "demo-model"},
            clear=True,
        ):
            config = config_module.load_config()

        self.assertEqual(config["max_retries"], 2)

    def test_rejects_missing_model_name(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(
                ValueError, "MODEL_NAME must be set and non-empty"
            ):
                config_module.load_config()

    def test_rejects_blank_model_name(self):
        with patch.dict(
            os.environ,
            {"MODEL_NAME": "   "},
            clear=True,
        ):
            with self.assertRaisesRegex(
                ValueError, "MODEL_NAME must be set and non-empty"
            ):
                config_module.load_config()

    def test_rejects_non_integer_retry_count(self):
        with patch.dict(
            os.environ,
            {"MODEL_NAME": "demo-model", "MAX_RETRIES": "abc"},
            clear=True,
        ):
            with self.assertRaisesRegex(
                ValueError, "MAX_RETRIES must be an integer"
            ):
                config_module.load_config()

    def test_rejects_negative_retry_count(self):
        with patch.dict(
            os.environ,
            {"MODEL_NAME": "demo-model", "MAX_RETRIES": "-1"},
            clear=True,
        ):
            with self.assertRaisesRegex(
                ValueError, "MAX_RETRIES must be non-negative"
            ):
                config_module.load_config()


if __name__ == "__main__":
    unittest.main()
