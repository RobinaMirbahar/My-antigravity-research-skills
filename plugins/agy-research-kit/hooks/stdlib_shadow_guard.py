"""Lifecycle hook preventing creation of files that shadow Python stdlib modules (e.g. numbers.py, math.py, statistics.py).

# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""

from pathlib import Path
import sys

FORBIDDEN_FILENAMES = {"numbers.py", "math.py", "statistics.py", "random.py", "types.py"}


def main() -> int:
    cwd = Path.cwd()
    clashes = [str(p) for name in FORBIDDEN_FILENAMES for p in cwd.glob(f"**/{name}") if ".venv" not in p.parts]
    if clashes:
        sys.stderr.write(
            f"[agy-research-kit Hook Warning] Stdlib-shadowing script detected ({clashes}). "
            "Rename to verify_math.py or eq_audit.py so NumPy/SciPy imports never break.\n"
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
