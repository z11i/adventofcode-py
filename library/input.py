from typing import List, Optional


def read(filename: Optional[str] = None) -> List[str]:
    if filename is None:
        filename = "input.txt"
    with open(filename) as f:
        lines = f.read().split("\n")[:-1]
        return lines
