from library.input import read


priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def priority_of_dupes(rucksack):
    n = len(rucksack)
    front, back = rucksack[: n // 2], rucksack[n // 2 :]
    return sum(priorities.find(c) for c in set(front) & set(back))


rucksacks = read()
print(sum(priority_of_dupes(rucksack) for rucksack in rucksacks))
