from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

if len(sys.argv) != 2:
    print("Usage: python scripts/run_problem.py s1p1.py")
    raise SystemExit(1)

path = ROOT / sys.argv[1]
if path.parent != ROOT or path.suffix != ".py" or not path.exists():
    print("Pick a Python file from the repo root")
    raise SystemExit(1)

raise SystemExit(subprocess.call([sys.executable, str(path)], cwd=ROOT))
