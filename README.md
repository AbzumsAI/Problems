# Code Solutions From Class

I use this repo as a small shelf for code I write while explaining math problems in class. Each script is meant to be read next to the problem statement, then run locally.

Most files follow this naming pattern:

- `s1p1.py` means session 1, problem 1.
- `s2p-scoring.py` means a scoring note for session 2.
- `func.py` is a short Python function example.

## Run A Script

Use Python 3. Install the packages once:

```bash
pip install -r requirements.txt
```

Run any problem file from the repo root:

```bash
python s1p1.py
```

Some scripts print symbolic answers with SymPy. A few scripts draw plots with NumPy and Matplotlib.

## Sessions

### Session 1: High School Math Review

- [Problem 1](s1p1.py)
- [Problem 2](s1p2.py)
- [Problem 3](s1p3.py)
- [Problem 4](s1p4.py)
- [Problem 5](s1p5.py)

### Session 2: Functions, Part 1

- [Problem 1](s2p1.py)
- [Problem 2](s2p2.py)
- [Problem 3](s2p3.py)
- [Problem 4](s2p4.py)
- [Problem 5](s2p5.py)
- [Problem 6](s2p6.py)
- [Problems 7 and 8](s2p7-8.py)
- [Problem 9](s2p9.py)
- [Problem 10](s2p10.py)
- [Problem 11](s2p11.py)
- [Scoring note](s2p-scoring.py)

### Session 3: Functions, Part 2

- [Problem 1](s3p1.py)
- [Problem 2](s3p2.py)
- [Scoring note](s3p-scoring.py)

### Session 4: Limits And Continuity, Part 1

- [Problem 1](s4p1.py)
- [Problem 2](s4p2.py)
- [Problem 3](s4p3.py)
- [Problem 4](s4p4.py)
- [Problem 5](s4p5.py)
- [Problem 6](s4p6.py)
- [Problem 7](s4p7.py)
- [Problem 8](s4p8.py)
- [Problem 9](s4p9.py)
- [Problem 10](s4p10.py)

The scoring files are still placeholders.

## Extra Notes

- `docs/problem-index.md` lists the Python files and sizes.
- `notes` has one short note for each script.
- `docs/running-scripts.md` explains how I run examples.
- `docs/review-check.md` is the check I use before committing code examples.
- `scripts/compile_problem_files.py` compiles the root Python files.
- `tests` has small checks for file names, requirements, and Python syntax.


