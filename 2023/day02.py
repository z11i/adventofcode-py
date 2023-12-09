from math import prod
from typing import List

import library.prelude as _

idx_map = {
    "red": 0,
    "green": 1,
    "blue": 2,
}


def parse(line: str):
    game_raw, records = line.split(": ")
    _, game_id = game_raw.split(" ")
    record_split = records.split("; ")
    all_counts = []
    for record in record_split:
        count_and_colors = record.split(", ")
        counts = [0, 0, 0]
        for count_and_color in count_and_colors:
            count, color = count_and_color.split(" ")
            counts[idx_map[color]] = int(count)
        all_counts.append(counts)
    return game_id, all_counts


def solve(input_data: List[str]):
    return sum(
        map(
            lambda x: int(x[0]),
            filter(
                lambda y: all(x[0] <= 12 and x[1] <= 13 and x[2] <= 14 for x in y[1]),
                map(parse, input_data),
            ),
        )
    )


def solve2(input_data: List[str]):
    return sum(
        [
            prod([max(values) for values in zip(*lists)])
            for _, lists in map(parse, input_data)
        ]
    )


inputs = _.read2()
_.p(solve(inputs.example))
_.p(solve(inputs.puzzle))
_.p(solve2(inputs.example))
_.p(solve2(inputs.puzzle))
