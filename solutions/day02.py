"""Advent of Code 2025 - Day XX"""


from __future__ import annotations
import re
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
    segments = []
    for segment in data:
        segments.extend(segment.split(','))
    filled_ranges = []
    for id_line in segments:
        start, end = map(int, id_line.split('-'))
        filled_ranges.append(range(start, end + 1))  # +1 if the end is inclusive
    #print(filled_ranges)
    repeating_nums = []
    for r in filled_ranges:
        for num in r:
            if len(str(num)) % 2 == 0:
                first_half =  str(num)[:int(len(str(num))/2)]
                second_half =  str(num)[int(len(str(num))/2):]
                if first_half == second_half:
                    repeating_nums.append(num)
    # print(repeating_nums)
    first_answer = 0
    for number in repeating_nums:
        first_answer += int(number)
    return first_answer


def solve_part2(data: Iterable[str]) -> int:
    """Solve part 2 of the puzzle."""

    REPEATED_BLOCK = re.compile(r"^(\d+)\1+$")
    segments: list[str] = []
    for line in data:
        for part in line.split(','):
            if part:
                segments.append(part)

    filled_ranges: list[range] = []
    for segment in segments:
        start, end = map(int, segment.split('-'))
        filled_ranges.append(range(start, end + 1))

    total = 0
    for r in filled_ranges:
        for num in r:
            if REPEATED_BLOCK.fullmatch(str(num)):
                total += num

    return total


def main() -> None:
    day = get_day_from_filename(__file__)
    raw = fetch_input(day)
    data = parse_input(raw)
    #print(data)
    print(f"Part 1: {solve_part1(data)}")
    print(f"Part 2: {solve_part2(data)}")


if __name__ == "__main__":
    main()
