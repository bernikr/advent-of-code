from __future__ import annotations

import operator
from collections import defaultdict
from itertools import product, islice


class Vec(tuple[int, ...]):
    def __new__(cls, *args: int | float) -> Vec:
        return super().__new__(cls, args)

    def __add__(self, other):
        return Vec(*map(operator.add, self, other))

    def __sub__(self, other):
        return Vec(*map(operator.sub, self, other))

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Vec(*map(lambda x: x * other, self))
        else:
            raise NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return Vec(*map(lambda x: x // other if x % other == 0 else x / other, self))
        else:
            raise NotImplemented


dirs4 = [Vec(0, -1), Vec(0, 1), Vec(1, 0), Vec(-1, 0)]
dirs8 = [Vec(*c) for c in product([-1, 0, 1], repeat=2) if c != (0, 0)]


def nth(iterable, n):
    return next(islice(iterable, n, None))


# Adapted from https://www.reddit.com/r/adventofcode/comments/rf7onx/2021_day_13_solutions/hocy115/
def ocr(m: set[tuple[int, int]]):
    mx, my = max(x for x, y in m), max(y for x, y in m)
    assert my == 5, "Letters need to be 5 rows high"
    s = ""
    for i in range(0, mx + 1, 5):
        v = int("".join('1' if (i + x, y) in m else '0' for y in range(6) for x in range(4)), 2)
        try:
            s += {6922137: "A", 15329694: "B", 6916246: "C", 16312463: "E", 16312456: 'F',
                  6917015: "G", 10090905: "H", 3215766: "J", 10144425: "K", 8947855: "L",
                  15310472: "P", 15310505: "R", 10066326: "U", 15803535: "Z"}[v]
        except KeyError:
            letter = '\n'.join("".join('▓' if (y, i + x) in m else ' ' for x in range(4)) for y in range(6))
            print(f"Unknown Letter with id {v}:\n\n{letter}")
            raise KeyError
    return s
