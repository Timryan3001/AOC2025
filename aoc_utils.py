"""Lightweight helpers for fetching Advent of Code inputs."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Optional

import requests
from dotenv import load_dotenv

DEFAULT_YEAR = 2025
INPUT_DIR = Path("inputs")
BASE_URL = "https://adventofcode.com/{year}/day/{day}/input"
USER_AGENT = "aoc2025-helper (+https://adventofcode.com)"

load_dotenv()


class AoCSessionMissing(RuntimeError):
    """Raised when the session cookie is not configured."""


def _get_session_cookie() -> str:
    session = os.getenv("AOC_SESSION") or os.getenv("SESSION")
    if not session:
        raise AoCSessionMissing(
            "Missing session cookie. Set AOC_SESSION (or SESSION) in your .env file."
        )
    return session.strip()


def get_input_path(day: int, *, input_dir: Path | str = INPUT_DIR) -> Path:
    """Return the expected path for the given day's input file."""
    if not 1 <= day <= 25:
        raise ValueError("day must be between 1 and 25")
    base = Path(input_dir)
    return base / f"day{day:02d}.txt"


def fetch_input(
    day: int,
    *,
    year: int = DEFAULT_YEAR,
    save_to_file: bool = True,
    input_dir: Path | str = INPUT_DIR,
    force: bool = False,
) -> str:
    """Download the input for `day`, optionally caching it on disk."""
    path = get_input_path(day, input_dir=input_dir)
    if path.exists() and not force:
        return path.read_text(encoding="utf-8").rstrip("\n")

    session_cookie = _get_session_cookie()
    url = BASE_URL.format(year=year, day=day)
    response = requests.get(
        url,
        cookies={"session": session_cookie},
        headers={"User-Agent": USER_AGENT},
        timeout=30,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"Failed to fetch input for day {day}: {response.status_code} {response.reason}"
        )

    input_text = response.text.rstrip("\n")
    if save_to_file:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(input_text + "\n", encoding="utf-8")
    return input_text


def ensure_input_file(
    day: int,
    *,
    year: int = DEFAULT_YEAR,
    input_dir: Path | str = INPUT_DIR,
    force: bool = False,
) -> Path:
    """Ensure the input file exists on disk and return its path."""
    fetch_input(day, year=year, save_to_file=True, input_dir=input_dir, force=force)
    return get_input_path(day, input_dir=input_dir)


def get_day_from_filename(filename: Optional[str] = None) -> int:
    """Extract the day number from a filename like 'day05.py'."""
    if filename is None:
        filename = os.path.basename(__file__)

    match = re.search(r"day(\d+)", filename, re.IGNORECASE)
    if not match:
        raise ValueError(
            "Could not find 'dayXX' in the filename. "
            "Ensure the script follows the day## naming convention."
        )
    return int(match.group(1).lstrip("0") or "0")


__all__ = [
    "fetch_input",
    "ensure_input_file",
    "get_input_path",
    "get_day_from_filename",
    "AoCSessionMissing",
]

