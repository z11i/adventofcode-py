import itertools
import math
from typing import List

import library.prelude as _


def parse(input_data: List[str]):
    gen_func = itertools.cycle(input_data[0])
    raw_edges_strs = input_data[2:]

    def split_edge(edge_str):
        a, b = edge_str.split(", ")
        return a[1:], b[:-1]

    edge_map = {
        k: split_edge(v) for line in raw_edges_strs for k, v in [line.split(" = ")]
    }
    return (gen_func, edge_map)


def steps_to_condition(edge_map, step_ops, curr, stop_condition):
    steps = 0
    while not stop_condition(curr):
        steps += 1
        op = next(step_ops)
        curr = edge_map[curr][0 if op == "L" else 1]
    return steps


def solve(input_data: List[str]):
    steps_gen, edge_map = parse(input_data)
    return steps_to_condition(edge_map, steps_gen, "AAA", lambda x: x == "ZZZ")


def solve2(input_data: List[str]):
    step_gen, edge_map = parse(input_data)
    currs = [x for x in edge_map.keys() if x.endswith("A")]

    return math.lcm(
        *map(
            lambda x: steps_to_condition(
                edge_map, step_gen, x, lambda y: y.endswith("Z")
            ),
            currs,
        )
    )


inputs = _.read2()
_.print(solve(inputs.example))
_.print(solve(inputs.puzzle))
_.print(solve2(inputs.example2))
_.print(solve2(inputs.puzzle))
