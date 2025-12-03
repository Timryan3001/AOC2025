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
    # splitting out the input so we have a nested list
    singular_nums = [list(line) for line in data]
    #print(singular_nums)

    # trimming the lists so we never pick the number at the end of the list
    trimmed_nums = []
    for numbers in singular_nums:
        shortened = numbers.copy()
        if shortened:
            shortened.pop()
        trimmed_nums.append(shortened)
    # print(trimmed_nums)

    # finding the highest number in the trimmed lists
    highest_nums = []
    for numbers in trimmed_nums:
        line_max = max(numbers)
        highest_nums.append(line_max)

    # print(highest_nums)

    # finding the index of the highest number in the trimmed list so we can then search for the second highest number after that
    after_highest = []

    for i in range(len(highest_nums)):
        highest = highest_nums[i]
        full_line = singular_nums[i]

        pos = full_line.index(highest)
        # print(f"line {i+1} number {highest} appears at index {pos}")

        # take everything after that position
        tail = full_line[pos + 1 :]
        after_highest.append(tail)

    # print(after_highest)

    #finding the highest number in the tails of the rows
    highest_in_tail = []
    for numbers in after_highest:
        line_max = max(numbers)
        highest_in_tail.append(line_max)
    # print(highest_in_tail)

    #combine the lists to get the highest number in each row
    combined_highest = []
    for i in range(len(highest_nums)):
        highest1 = str(highest_nums[i])
        highest2 = str(highest_in_tail[i])

        combined = int(highest1+highest2)
        combined_highest.append(combined)
    #print(combined_highest)
    part1_answer = sum(combined_highest)

    return part1_answer


def solve_part2(data: Iterable[str]) -> int:
    """Solve part 2 of the puzzle."""
    
    total = 0
    #get the digits from each line
    for line in data:
        digits = list(line)
        target_count = 12
        
        # aiming to remove smaller digits from left when we see larger ones
        to_remove = len(digits) - target_count
        result = []
        
        for digit in digits:
            # While we can still remove digits and the current digit is larger than the last digit in our result, remove the last one
            while to_remove > 0 and result and result[-1] < digit:
                result.pop()
                to_remove -= 1
            result.append(digit)
        
        # If we still need to remove more digits, remove from the end 1 by 1
        while len(result) > target_count:
            result.pop()
        
        num_str = ''.join(result)
        total += int(num_str)
    
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
