from typing import List, Optional


def read(filename: Optional[str] = None, ignore_last: bool = False) -> List[str]:
    if filename is None:
        filename = "input.txt"
    with open(filename) as f:
        lines = f.read().split("\n")
        if ignore_last:
            lines = lines[:-1]
        return lines
