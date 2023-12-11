import pprint
from typing import Sequence


def p(obj, *args, **kwargs):
    if hasattr(obj, "__iter__"):
        obj = list(obj)
    pprint.pprint(obj, *args, **kwargs)
    return obj


def listdbg(lst: Sequence, *args, **kwargs):
    """
    Print the list with some debug info.
    listdbg(lst, i=i) prints the i-th element.
    listdbg(lst, _range=(i, j)) prints the slice lst[i:j].
    """
    s = ""
    for arg in args:
        s = s + arg + " "

    s_func = lambda x: ",".join(map(str, x))  # noqa: E731
    if (strategy := kwargs.get("_s")) is not None:
        if strategy == 0:
            s_func = lambda x: "".join(map(str, x))  # noqa: E731
        else:
            s_func = strategy

    lst_str = s_func(lst)
    s += f"[{lst_str}]\tlen={len(lst)}"
    for kwk, kwv in kwargs.items():
        if not kwk.startswith("_"):
            try:
                v = lst[int(kwv)]
            except IndexError:
                v = "(OUT)"
            s += f"\n\t{kwk}({kwv})={v}"
        elif kwk == "_range":
            v = lst[kwv[0] : min(len(lst), kwv[1])]
            s += f"\n\t{kwv[0]}~{kwv[1]}={listdbg(v, _s=s_func, _nested=1)}"
            if kwv[1] > len(lst):
                s += " (TRUNCATED)"

    if "_nested" not in kwargs:
        print(s)
    return s


if __name__ == "__main__":
    listdbg("abcdefg", i=0, _range=(2, 5))
