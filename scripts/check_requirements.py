from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / "requirements.txt").read_text(encoding="utf-8")
packages = {line.split("==", 1)[0].strip().lower() for line in text.splitlines() if line.strip()}
required = {"matplotlib", "numpy", "sympy"}
missing = sorted(required - packages)

if missing:
    print("Missing packages: " + ", ".join(missing))
    raise SystemExit(1)

print("Requirements check passed")
