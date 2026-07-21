from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RequirementsFileTest(unittest.TestCase):
    def test_expected_packages_are_listed(self):
        text = (ROOT / "requirements.txt").read_text(encoding="utf-8")
        packages = {line.split("==", 1)[0].strip().lower() for line in text.splitlines() if line.strip()}
        self.assertIn("matplotlib", packages)
        self.assertIn("numpy", packages)
        self.assertIn("sympy", packages)


if __name__ == "__main__":
    unittest.main()
