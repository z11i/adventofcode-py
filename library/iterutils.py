import itertools
from typing import Callable, Iterable, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def groupwise(iterable: Iterable[T], n: int, f: Callable[[Iterable[T]], R] = tuple):
    """
    Iterate over iterable in groups of n. `f` transform the group before yielding.
    list(groupwise('ABCDEFG', 3, tuple)) --> [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]
    """

    if n == 2:
        return itertools.pairwise(iterable)
    it = iter(iterable)
    while True:
        chunk = f(itertools.islice(it, n))
        if not chunk:
            break
        yield chunk


class defaultlist(list):
    """A list that can be indexed with values that are larger than the length of the list."""

    def __init__(self, fx):
        self._fx = fx

    def _fill(self, index):
        while len(self) <= index:
            self.append(self._fx())

    def __setitem__(self, index, value):
        self._fill(index)
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        self._fill(index)
        return list.__getitem__(self, index)
