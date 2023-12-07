from library.input import read
from library import iterutils


priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def priority_of_dupes(rucksack):
    n = len(rucksack)
    front, back = rucksack[: n // 2], rucksack[n // 2 :]
    return sum(priorities.find(c) for c in set(front) & set(back))


# part 1
rucksacks = read()
print(sum(priority_of_dupes(rucksack) for rucksack in rucksacks))

# part 2
groups_of_3 = iterutils.groupwise(rucksacks, 3, tuple)
print(
    sum(
        priorities.find(c)
        for r1, r2, r3 in groups_of_3
        for c in set(r1) & set(r2) & set(r3)
    )
)
