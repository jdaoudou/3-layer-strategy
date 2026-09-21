import argparse
import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "cli" / "three_layer.py"
SPEC = importlib.util.spec_from_file_location("three_layer", MODULE_PATH)
three_layer = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(three_layer)


class ThreeLayerCliTests(unittest.TestCase):
    def test_init_and_doctor(self):
        with tempfile.TemporaryDirectory() as directory:
            args = argparse.Namespace(path=directory, adapter="all", force=False)
            self.assertEqual(three_layer.command_init(args), 0)
            project = Path(directory)
            self.assertTrue((project / ".aidd/config.yaml").is_file())
            self.assertTrue((project / "AGENTS.md").is_file())
            self.assertTrue((project / "CLAUDE.md").is_file())
            self.assertEqual(three_layer.doctor_errors(project), [])

    def test_new_change_renders_bundle(self):
        with tempfile.TemporaryDirectory() as directory:
            three_layer.command_init(argparse.Namespace(path=directory, adapter="none", force=False))
            result = three_layer.command_new_change(
                argparse.Namespace(
                    slug="improve-search",
                    project=directory,
                    title="Improve search",
                    owner="Product",
                    force=False,
                )
            )
            self.assertEqual(result, 0)
            change = Path(directory) / ".aidd/changes/improve-search"
            self.assertEqual(sorted(path.name for path in change.iterdir()), sorted(three_layer.CHANGE_FILES))
            self.assertIn("Improve search", (change / "intent.md").read_text(encoding="utf-8"))
            self.assertEqual(three_layer.doctor_errors(Path(directory)), [])

    def test_rejects_invalid_slug(self):
        with tempfile.TemporaryDirectory() as directory:
            three_layer.command_init(argparse.Namespace(path=directory, adapter="none", force=False))
            result = three_layer.command_new_change(
                argparse.Namespace(slug="Not valid", project=directory, title="X", owner="Y", force=False)
            )
            self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
