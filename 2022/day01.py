import itertools
from library.input import read


def solve(lines):
    return max(
        [
            sum(list(map(lambda x: int(x), group)))
            for k, group in itertools.groupby(lines, lambda x: x == "")
            if not k
        ]
    )


def solve_part_2(lines):
    return sum(
        sorted(
            [
                sum(list(map(lambda x: int(x), group)))
                for k, group in itertools.groupby(lines, lambda x: x == "")
                if not k
            ],
            reverse=True,
        )[:3]
    )


if __name__ == "__main__":
    data = read()
    print(solve_part_2(data))
