from __future__ import annotations

import operator
from math import sqrt
from enum import Enum
from heapq import heappush, heappop
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

    def __rmul__(self, other):
        if isinstance(other, int | float):
            return Vec(*map(lambda x: x * other, self))
        else:
            raise NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return Vec(*map(lambda x: x // other if x % other == 0 else x / other, self))
        else:
            raise NotImplemented

    def __abs__(self):
        return sqrt(sum(x*x for x in self))

    def manhatten(self):
        return sum(abs(x) for x in self)


dirs4 = [Vec(0, -1), Vec(0, 1), Vec(1, 0), Vec(-1, 0)]
dirs8 = [Vec(*c) for c in product([-1, 0, 1], repeat=2) if c != (0, 0)]


class Dir(Enum):
    UP = Vec(0, -1)
    DOWN = Vec(0, 1)
    LEFT = Vec(-1, 0)
    RIGHT = Vec(1, 0)

    def turn_left(self):
        return Dir((self.value[1], -self.value[0]))

    def turn_right(self):
        return Dir((-self.value[1], self.value[0]))


class Rect:
    def __init__(self, *corners):
        self.lower = Vec(*(min(a[i] for a in corners) for i in range(len(corners[0]))))
        self.upper = Vec(*(max(a[i] for a in corners) for i in range(len(corners[0]))))

    def __contains__(self, item):
        return all(mi <= i <= ma for mi, ma, i in zip(self.lower, self.upper, item))

    def __repr__(self):
        return f"Rect{{{self.lower}...{self.upper}}}"

    @property
    def center(self):
        return Vec(*((mi + ma) / 2 for mi, ma in zip(self.lower, self.upper)))


def nth(iterable, n):
    return next(islice(iterable, n, None))


# Adapted from https://www.reddit.com/r/adventofcode/comments/rf7onx/2021_day_13_solutions/hocy115/
def ocr(m: set[tuple[int, int]]):
    mx, my = max(x for x, y in m), max(y for x, y in m)
    assert my == 5, "Letters need to be 6 rows high"
    s = ""
    for i in range(0, mx + 1, 5):
        v = int("".join('1' if (i + x, y) in m else '0' for y in range(6) for x in range(4)), 2)
        try:
            s += {6922137: "A", 15329694: "B", 6916246: "C", 16312463: "E", 16312456: 'F', 6917015: "G", 10090905: "H",
                  3215766: "J", 10144425: "K", 8947855: "L", 6920598: "O", 15310472: "P", 15310505: "R", 7898654: "S",
                  10066326: "U", 15803535: "Z"}[v]
        except KeyError:
            letter = '\n'.join("".join('▓' if (i + x, y) in m else ' ' for x in range(4)) for y in range(6))
            print(f"Unknown Letter with id {v}:\n\n{letter}")
            raise KeyError
    return s


class PriorityQueue:
    def __init__(self):
        self.items = []
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def put(self, item, priority):
        self.items.append(item)
        heappush(self.queue, (priority, len(self.items) - 1))

    def get(self):
        return self.items[heappop(self.queue)[1]]


class CircularList(list):
    def __getitem__(self, item):
        if isinstance(item, int):
            return super(CircularList, self).__getitem__(item % len(self))
        elif isinstance(item, slice):
            return list(self[i] for i in range(
                item.start if item.start is not None else 0,
                item.stop if item.stop is not None else len(self),
                item.step if item.step is not None else 1
            ))
        else:
            raise NotImplementedError()

    def __setitem__(self, key, value):
        if isinstance(key, int):
            return super(CircularList, self).__setitem__(key % len(self), value)
        elif isinstance(key, slice):
            keys = list(range(
                key.start if key.start is not None else 0,
                key.stop if key.stop is not None else len(self),
                key.step if key.step is not None else 1
            ))
            if len(keys) != len(value):
                raise NotImplementedError(
                    "CircularList: Replacing slices of different length is currently not implemented")
            for k, v in zip(keys, value):
                self[k] = v
        else:
            raise NotImplementedError()


def sign(x):
    return x and (1, -1)[x < 0]
