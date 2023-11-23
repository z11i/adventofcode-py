import itertools


def groupwise(iterable, n):
    """Iterate over iterable in groups of n."""
    if n == 2:
        return itertools.pairwise(iterable)
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            break
        yield chunk
