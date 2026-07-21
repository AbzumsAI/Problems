from pathlib import Path
import py_compile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CompileProblemFilesTest(unittest.TestCase):
    def test_root_problem_files_compile(self):
        for path in sorted(ROOT.glob("*.py")):
            with self.subTest(path=path.name):
                py_compile.compile(str(path), doraise=True)


if __name__ == "__main__":
    unittest.main()
