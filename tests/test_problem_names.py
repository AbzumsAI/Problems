from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"s\d+p(\d+|\d+-\d+|-scoring)\.py")


class ProblemNameTest(unittest.TestCase):
    def test_problem_file_names_follow_pattern(self):
        for path in sorted(ROOT.glob("s*.py")):
            with self.subTest(path=path.name):
                self.assertRegex(path.name, PATTERN)


if __name__ == "__main__":
    unittest.main()
