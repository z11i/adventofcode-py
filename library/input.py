from dataclasses import dataclass
import sys
from typing import List, Optional, TextIO, TypedDict


@dataclass
class InputResult:
    example: List[str]
    puzzle: List[str]
    example2: Optional[List[str]] = None


def read(filename: Optional[str] = None) -> List[str]:
    if filename is None:
        filename = "input.txt"
    with open(filename) as f:
        lines = f.read().split("\n")[:-1]
        return lines


def read2(year: Optional[int] = None, day: Optional[int] = None) -> InputResult:
    # when called like `python3 -m 2022.day04`, sys.argv looks like:
    # ['/Users/z11i/adventofcode-py/2022/day04.py']
    year_str, day_str = sys.argv[0].split("/")[-2:]
    if year and day:
        year_str, day_str = f"{year:02}", f"{day:02}"
    day_input_prefix = "/input/".join([year_str, day_str]).split(".")[0]
    input_path = f"{day_input_prefix}.input"
    sample_path = f"{day_input_prefix}.example"
    sample_path2 = f"{day_input_prefix}.example2"

    def r(f: TextIO):
        lines = f.read().split("\n")
        for i in range(len(lines) - 1, -1, -1):
            if lines[i] != "":
                return lines[: i + 1]
        return lines

    with open(input_path) as fi, open(sample_path) as fs:
        ir = InputResult(example=r(fs), puzzle=r(fi))
    try:
        with open(sample_path2) as fs:
            ir.example2 = r(fs)
    except FileNotFoundError:
        pass
    return ir
