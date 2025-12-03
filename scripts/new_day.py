"""Change DAY below and click 'Run' to scaffold a solution file for that day.

This script:
- Ensures the input for that day is downloaded.
- Creates `solutions/dayXX.py` if it does not already exist.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from aoc_utils import ensure_input_file  # noqa: E402

DAY = 3  # <- change this each time you want to scaffold a new day (1–25)

SOLUTION_TEMPLATE = """\"\"\"Advent of Code 2025 - Day XX\"\"\"

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from aoc_utils import fetch_input, get_day_from_filename


def parse_input(raw: str) -> list[str]:
    \"\"\"Convert the raw puzzle input into a structured representation.\"\"\"
    return raw.strip().splitlines()


def solve_part1(data: Iterable[str]) -> int:
    \"\"\"Solve part 1 of the puzzle.\"\"\"
    # TODO: implement the actual solution
    return 0


def solve_part2(data: Iterable[str]) -> int:
    \"\"\"Solve part 2 of the puzzle.\"\"\"
    # TODO: implement the actual solution
    return 0


def main() -> None:
    day = get_day_from_filename(__file__)
    raw = fetch_input(day)
    data = parse_input(raw)
    print(f"Part 1: {solve_part1(data)}")
    print(f"Part 2: {solve_part2(data)}")


if __name__ == "__main__":
    main()
"""


def main() -> None:
    if not 1 <= DAY <= 25:
        raise ValueError("DAY must be between 1 and 25")

    # Make sure the input is present on disk
    ensure_input_file(DAY)

    # Create the solution file for this day if needed
    solutions_dir = PROJECT_ROOT / "solutions"
    solutions_dir.mkdir(parents=True, exist_ok=True)

    solution_path = solutions_dir / f"day{DAY:02d}.py"
    if solution_path.exists():
        print(f"{solution_path} already exists, not overwriting.")
        return

    solution_path.write_text(SOLUTION_TEMPLATE, encoding="utf-8")
    print(f"Created {solution_path}")


if __name__ == "__main__":
    main()


