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
    #find how many rows by just counting how many things there are within the data list
    rows = len(data)
    #find how many columns by just counting how many things there are within the first row
    cols = len(data[0])
    print(rows)
    print(cols)
    print(data)
    
    #we'll use this to count how many accessible positions there are incrementing when we find something suitable
    accessible_count = 0
    
    # Directions
    directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
    
    #loop through each row
    for i in range(rows):
        #loop through each column
        for j in range(cols):
            #if the current position is not an @, we can skip it
            if data[i][j] != '@':
                continue
            
            # Count @ symbols in adjacent positions
            neighbor_count = 0
            # we now look at every position around the current position and check if it is an @
            for row_offset, col_offset in directions:
                neighbor_row = i + row_offset
                neighbor_col = j + col_offset
                # Check bounds so we dont get errors going out of bounds
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    if data[neighbor_row][neighbor_col] == '@':
                        neighbor_count += 1
            
            # Accessible if fewer than 4 neighbors are @
            if neighbor_count < 4:
                accessible_count += 1
    
    return accessible_count


def solve_part2(data: Iterable[str]) -> int:
    """Solve part 2 of the puzzle."""
    grid = [list(row) for row in data]
    
    #find how many rows by just counting how many things there are within the data list
    rows = len(grid)
    #find how many columns by just counting how many things there are within the first row
    cols = len(grid[0])
    # Directions
    directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
    
    # Total count of all accessible rolls removed across all iterations
    total_accessible_count = 0
    
    # Keep looping while we find accessible rolls
    while True:
        # Track how many accessible rolls we find in this pass
        accessible_in_this_pass = 0
        # Store positions to replace after the loop is ran so as not to mess up the logic of the loop idk this might be slow but seems methodical
        positions_to_replace = []
        
        #loop through each row
        for i in range(rows):
            #loop through each column
            for j in range(cols):
                #if the current position is not an @, we can skip it
                if grid[i][j] != '@':
                    continue
                
                # Count @ symbols in adjacent positions
                neighbor_count = 0
                # we now look at every position around the current position and check if it is an @
                for row_offset, col_offset in directions:
                    neighbor_row = i + row_offset
                    neighbor_col = j + col_offset
                    # Check bounds so we dont get errors going out of bounds
                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                        if grid[neighbor_row][neighbor_col] == '@':
                            neighbor_count += 1
                
                # Accessible if fewer than 4 neighbors are @
                if neighbor_count < 4:
                    accessible_in_this_pass += 1
                    positions_to_replace.append((i, j))
        
        # If we didn't find any accessible rolls, we're done
        if accessible_in_this_pass == 0:
            break
        
        # Replace all accessible rolls with '.' in this pass
        for row, col in positions_to_replace:
            grid[row][col] = '.'
        
        # Add to our total count
        total_accessible_count += accessible_in_this_pass
    
    return total_accessible_count

def main() -> None:
    day = get_day_from_filename(__file__)
    raw = fetch_input(day)
    data = parse_input(raw)
    #print(data)
    print(f"Part 1: {solve_part1(data)}")
    print(f"Part 2: {solve_part2(data)}")


if __name__ == "__main__":
    main()
