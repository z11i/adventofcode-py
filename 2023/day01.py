from typing import List

import library.prelude as _
from library.debug import listdbg

inputs = _.read2()


def solve(input_data: List[str]):
    def process_line(line):
        lst = list(filter(lambda c: c.isdigit(), line))
        return int(lst[0]) * 10 + int(lst[-1])

    return sum(map(process_line, input_data))


def solve2(input_data: List[str]):
    replace_map = {
        3: {
            "one": "o1e",
            "two": "t2o",
            "six": "s6x",
        },
        4: {
            "four": "f4r",
            "five": "f5e",
            "nine": "n9e",
        },
        5: {
            "three": "t3e",
            "seven": "s7n",
            "eight": "e8t",
        },
    }

    def process_line(line):
        L = len(line)
        i = 0
        while i <= L - 3:
            replaced = False
            for j in range(3, 6):
                if i + j > L:
                    break
                # listdbg(line, i=i, j=j, _range=(i, i + j), _s=0)
                if line[i : i + j] in replace_map[j]:
                    line = line[:i] + replace_map[j][line[i : i + j]] + line[i + j :]
                    replaced = True
                    L = len(line)
                    # listdbg(line, "REPLACED", i=i, j=j, _range=(i, i + j), _s=0)
                    break
            i += 2 if replaced else 1

        lst = list(filter(lambda c: c.isdigit(), line))
        print(lst)
        return int(lst[0]) * 10 + int(lst[-1])

    return sum(map(process_line, input_data))


_.p(solve(inputs.example))
_.p(solve(inputs.puzzle))
_.p(solve2(inputs.example2))
# _.p(solve2(["eightwo"]))
_.p(solve2(inputs.puzzle))
