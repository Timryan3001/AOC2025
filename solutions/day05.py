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
    halves = raw.split('\n\n')
    ranges = halves[0].split('\n')
    ids = halves[1].split('\n')
    return ranges, ids


def solve_part1(data: Iterable[str]) -> int:
    """Solve part 1 of the puzzle."""
    print("starting problem")

#--------------------------------attempt 1--------------------------------#
    #create a list we can fill in with all the valid ids
    # valid_ids = []
    # ranges, ids = data
    # #split out the ranges add all numbers within ranges to list
    # for r in ranges:
    #     lower = r.split('-')[0]
    #     upper = int(r.split('-')[1])+1
    #     for number in range(int(lower), int(upper)):
    #         if number not in valid_ids:
    #             valid_ids.append(number)
    # # print(valid_ids)
    
    # valid_ids_count = 0
    # for id in ids:
    #     if int(id) in valid_ids:  # Convert id to int and check for empty string
    #         valid_ids_count += 1
    # print(valid_ids_count)
    # return valid_ids_count
#--------------------------------attempt 1--------------------------------#

    valid_ids_count = 0
    ranges, ids = data
    for number in ids:
        for r in ranges:
            lower = int(r.split('-')[0])
            upper = int(r.split('-')[1])+1
            if int(number) in range(lower, upper):
                valid_ids_count += 1
                break  #stop checking other ranges once we find a match
    return valid_ids_count

def solve_part2(data: Iterable[str]) -> int:
    """Solve part 2 of the puzzle."""
    ranges, ids = data
    # Parse all ranges into (start, end) tuples
    intervals = []
    for r in ranges:
        parts = r.split('-')
        start = int(parts[0])
        end = int(parts[1])
        intervals.append((start, end))
    
    # Sort intervals by start value
    intervals.sort(key=lambda x: x[0])
    
    # Merge overlapping intervals
    merged = []
    for start, end in intervals:
        if not merged:
            merged.append([start, end])
        else:
            last_start, last_end = merged[-1]
            # If current interval overlaps or is adjacent to the last one
            if start <= last_end + 1:  # +1 for adjacent intervals
                # Merge by extending the end if needed
                merged[-1][1] = max(last_end, end)
            else:
                # No overlap, add as new interval
                merged.append([start, end])
    
    # Calculate total count: sum of (end - start + 1) for each merged interval
    total = sum(end - start + 1 for start, end in merged)
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
