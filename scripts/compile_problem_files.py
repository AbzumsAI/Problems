from pathlib import Path
import py_compile

ROOT = Path(__file__).resolve().parents[1]
files = sorted(ROOT.glob("*.py"))

for path in files:
    py_compile.compile(str(path), doraise=True)

print(f"Compiled {len(files)} problem files")
