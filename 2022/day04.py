import library.prelude as _


def line_to_range_pair(line: str):
    # turns "1-3,2-5" into [(1,3),(2,5)]
    return tuple(tuple(map(int, r.split("-"))) for r in line.split(","))


def fully_overlapped(r0: tuple, r1: tuple):
    return (r0[0] <= r1[0] and r0[1] >= r1[1]) or (r1[0] <= r0[0] and r1[1] >= r0[1])


def partially_overlapped(r0: tuple, r1: tuple):
    return (
        (r0[0] <= r1[0] and r0[1] >= r1[0])
        or (r1[0] <= r0[0] and r1[1] >= r0[0])
        or (r0[0] <= r1[1] and r0[1] >= r1[1])
        or (r1[0] <= r0[1] and r1[1] >= r0[1])
    )


_.p(
    sum(
        fully_overlapped(r1, r2)
        for line in _.read()
        for r1, r2 in [line_to_range_pair(line)]
    )
)

_.p(
    sum(
        partially_overlapped(r1, r2)
        for line in _.read()
        for r1, r2 in [line_to_range_pair(line)]
    )
)
