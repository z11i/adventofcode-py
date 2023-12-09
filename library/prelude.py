from .input import read, read2
from pprint import pprint


def p(obj, *args, **kwargs):
    if hasattr(obj, "__iter__"):
        obj = list(obj)
    pprint(obj, *args, **kwargs)


__all__ = ["read", "read2", "p"]
