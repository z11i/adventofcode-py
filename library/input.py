from typing import List, Optional


def read(filename: Optional[str] = None) -> List[str]:
    if filename is None:
        filename = "input.txt"
    with open(filename) as f:
        return f.read().split("\n")
