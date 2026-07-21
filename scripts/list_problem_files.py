from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

for path in sorted(ROOT.glob("*.py")):
    print(f"{path.name}\t{path.stat().st_size} bytes")
