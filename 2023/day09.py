import itertools
from typing import List

import library.prelude as _


def find_inter_diff(nums: List[int]):
    return [x2 - x1 for (x1, x2) in itertools.pairwise(nums)]


def until(xs, pred, transform=lambda xs: xs):
    history = []
    while not pred(xs):
        history.append(xs)
        xs = transform(xs)
    history.append(xs)
    return history


def until_zeroes(xs):
    xs = [int(x) for x in xs if x != " "]
    return until(xs, lambda xs: all(x == 0 for x in xs), lambda xs: find_inter_diff(xs))


def add_tails(ls):
    return sum(xs[-1] for xs in ls)


def subtract_head_from_backwards(ls):
    diff = ls[-2][0] - ls[-1][0]
    for i in range(len(ls) - 3, -1, -1):
        diff = ls[i][0] - diff
    return diff


def solve(input_data: List[str]):
    return sum(
        map(add_tails, map(until_zeroes, map(lambda x: x.split(" "), input_data)))
    )


def solve2(input_data: List[str]):
    subproblems = map(lambda x: x.split(" "), input_data)
    proceduces = map(until_zeroes, subproblems)
    return sum(map(subtract_head_from_backwards, proceduces))


inputs = _.read2()
_.p(solve(inputs.example))
_.p(solve(inputs.puzzle))
_.p(solve2(inputs.example))
_.p(solve2(inputs.puzzle))
