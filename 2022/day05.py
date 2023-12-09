from typing import Iterable, List, Tuple
from library.iterutils import defaultlist, groupwise
import library.prelude as __

input_data = __.read2()


def parse(lines: List[str]) -> Iterable[defaultlist | Tuple[str, str, str]]:
    stacks = defaultlist(list)
    stacks_returned = False
    for line in lines:
        if line == "":
            continue
        elif "[" in line:
            for i, box in enumerate(groupwise(line, 4, lambda x: "".join(x))):
                if "[" in box:
                    stacks[i].insert(0, box[1])
        elif "move" in line:
            if not stacks_returned:
                yield stacks
                stacks_returned = True
            ws = line.split(" ")
            yield (ws[1], ws[3], ws[5])


def solve(data_gen):
    p = parse(data_gen)
    stacks: defaultlist = next(p)
    for moves, src, dst in p:
        src_i = int(src) - 1
        dst_i = int(dst) - 1
        for _ in range(int(moves)):
            stacks[dst_i].append(stacks[src_i].pop())
    return "".join([s[-1] for s in stacks if len(s) > 0])


def solve2(data_gen):
    p = parse(data_gen)
    stacks: defaultlist = next(p)
    for moves, src, dst in p:
        src_i = int(src) - 1
        dst_i = int(dst) - 1
        stacks[dst_i].extend(stacks[src_i][-int(moves) :])
        stacks[src_i] = stacks[src_i][: -int(moves)]
    return "".join([s[-1] for s in stacks if len(s) > 0])


__.p(solve(input_data.example))
__.p(solve(input_data.puzzle))
__.p(solve2(input_data.example))
__.p(solve2(input_data.puzzle))
