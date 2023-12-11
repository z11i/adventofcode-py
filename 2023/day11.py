from dataclasses import dataclass
import itertools
from typing import List, Tuple

import library.prelude as _


@dataclass
class Point:
    r: int
    c: int


def parse(input_data: List[str]):
    return [[c for c in x] for x in input_data]


# def expand_matrix_on_empty(matrix: List[List[str]]):
#     i, R = 0, len(matrix)
#     while i < R:
#         if all(x == "." for x in matrix[i]):
#             R += 1
#             matrix.insert(i, ["."] * len(matrix[i]))
#             i += 1
#         i += 1
#     j, C = 0, len(matrix[0])
#     while j < C:
#         if all(x == "." for x in [matrix[i][j] for i in range(R)]):
#             C += 1
#             for i in range(R):
#                 matrix[i].insert(j, ".")
#             j += 1
#         j += 1
#     return matrix


def find_empty_spaces(matrix: List[List[str]]) -> Tuple[List[int], List[int]]:
    empty_rows_prefix_sum = [0] * (len(matrix) + 1)
    empty_cols_prefix_sum = [0] * (len(matrix[0]) + 1)

    for r in range(len(matrix)):
        if all(x == "." for x in matrix[r]):
            empty_rows_prefix_sum[r + 1] = empty_rows_prefix_sum[r] + 1
        else:
            empty_rows_prefix_sum[r + 1] = empty_rows_prefix_sum[r]
    for c in range(len(matrix[0])):
        if all(x == "." for x in [matrix[i][c] for i in range(len(matrix))]):
            empty_cols_prefix_sum[c + 1] = empty_cols_prefix_sum[c] + 1
        else:
            empty_cols_prefix_sum[c + 1] = empty_cols_prefix_sum[c]
    return (empty_rows_prefix_sum[1:], empty_cols_prefix_sum[1:])


def find_galaxies(space: List[List[str]]) -> List[Point]:
    return [
        Point(r, c)
        for r in range(len(space))
        for c in range(len(space[0]))
        if space[r][c] == "#"
    ]


def find_shortest_path(
    empty_rows_prefix_sum, empty_cols_prefix_sum, start: Point, end: Point, multiplier
) -> int:
    ans = (
        abs(start.r - end.r)
        + abs(empty_rows_prefix_sum[start.r] - empty_rows_prefix_sum[end.r])
        * (multiplier - 1)
        + abs(start.c - end.c)
        + abs(empty_cols_prefix_sum[start.c] - empty_cols_prefix_sum[end.c])
        * (multiplier - 1)
    )
    return ans


def _solve(input_data: List[str], multiplier):
    space = parse(input_data)
    galaxies = find_galaxies(space)
    empty_rows_prefix_sum, empty_cols_prefix_sum = find_empty_spaces(space)
    pairs = itertools.combinations(galaxies, 2)
    return sum(
        find_shortest_path(
            empty_rows_prefix_sum, empty_cols_prefix_sum, *pair, multiplier
        )
        for pair in pairs
    )


def solve(input_data: List[str]):
    return _solve(input_data, 2)


def solve2(input_data: List[str]):
    return _solve(input_data, 1000000)


inputs = _.read2()
_.p(solve(inputs.example))
_.p(solve(inputs.puzzle))
_.p(solve2(inputs.example))
_.p(solve2(inputs.puzzle))
