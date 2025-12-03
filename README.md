# Advent of Code 2025 Helper

Utilities for downloading puzzle inputs and scaffolding daily Python solutions.

## Setup

1. Create a virtual environment (optional but recommended) and install deps:
   ```
   pip install -r requirements.txt
   ```
2. Copy your Advent of Code session cookie into a `.env` file in this folder:
   ```
   AOC_SESSION=your_session_cookie_here
   ```
   The value comes from the `session` cookie after logging in at [adventofcode.com](https://adventofcode.com). Keep it private.

## Usage

- **Fetch input and scaffold a solution stub:**
  ```
  python scripts/new_day.py 1
  ```
  This downloads `inputs/day01.txt` (if missing) and creates `solutions/day01.py` using the default template.
- **Re-download an input:** add `--force-input`.
- Each solution file includes `parse_input`, `solve_part1`, `solve_part2`, and a `main()` helper that prints both answers.

## Project Layout

- `aoc_utils/fetch_aoc_input.py` – handles `.env` loading and authenticated downloads.
- `scripts/new_day.py` – CLI for managing daily scaffolding.
- `inputs/` – cached puzzle inputs (not checked in).
- `solutions/` – where you implement each day's answers.

Feel free to customize the template or extend the tooling as the event progresses!

