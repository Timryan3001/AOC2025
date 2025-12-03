"""Advent of Code 2025 - Day XX"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from aoc_utils import fetch_input, get_day_from_filename


def parse_input(raw: str) -> list[str]:
    """Convert the raw puzzle input into a structured representation."""
    return raw.strip().splitlines()


def solve_part1(data: Iterable[str]) -> int:
    """Solve part 1 of the puzzle."""
    start = 50
    zeroed = 0
    moves = [(step[0], step[1:]) for step in data]

    for direction, amount in moves:
        amount = int(amount)
        if direction == 'R':
            start += amount
        else:
            start -= amount

        start = start % 100

        if start == 0:
            zeroed +=1
    return zeroed


def solve_part2(data: Iterable[str]) -> int:
    """Solve part 2 of the puzzle."""
    start = 50
    zeroed_part2 = 0
    moves = [(step[0], step[1:]) for step in data]

    for direction, amount_str in moves:
        amount = int(amount_str)
        dir_sign = 1 if direction == 'R' else -1

        if dir_sign == 1:
            first_zero = 100 if start == 0 else 100 - start
        else:
            first_zero = 100 if start == 0 else start

        if amount >= first_zero:
            zeroed_part2 += 1 + (amount - first_zero) // 100

        start = (start + dir_sign * amount) % 100

    return zeroed_part2


def main() -> None:
    day = get_day_from_filename(__file__)
    raw = fetch_input(day)
    data = parse_input(raw)
    #print(data)
    print(f"Part 1: {solve_part1(data)}")
    print(f"Part 2: {solve_part2(data)}")


if __name__ == "__main__":
    main()
