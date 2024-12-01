from __future__ import annotations

import math
import operator
from collections import defaultdict
from functools import reduce
from math import sqrt
from enum import Enum
from heapq import heappush, heappop
from itertools import product, islice
import portion

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
            raise NotImplementedError()

    def __rmul__(self, other):
        if isinstance(other, int | float):
            return Vec(*map(lambda x: x * other, self))
        else:
            raise NotImplementedError()

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return Vec(*map(lambda x: x // other if x % other == 0 else x / other, self))
        else:
            raise NotImplementedError()

    def __abs__(self):
        return sqrt(sum(x * x for x in self))

    def pos_mod(self, other):
        if isinstance(other, int):
            other = Vec(*((other,) * len(self)))
        if isinstance(other, Vec):
            return Vec(*map(lambda s, o: (s % o + o) % o, self, other))
        else:
            raise NotImplementedError()

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


DOWN = Dir.DOWN.value
LEFT = Dir.LEFT.value
RIGHT = Dir.RIGHT.value
UP = Dir.UP.value


class Matrix(tuple[tuple[int, ...], ...]):
    def __new__(cls, *args: tuple[int, ...]) -> Matrix:
        return super().__new__(cls, args)

    def __add__(self, other):
        raise NotImplementedError()

    def __mul__(self, other):
        if isinstance(other, Vec):
            return Vec(*map(lambda row: sum(a * b for a, b in zip(row, other)), self))
        elif isinstance(other, Matrix):
            assert len(self[0]) == len(other)
            return Matrix(*map(lambda s_row: tuple(sum(s_row[i] * other[i][column_i] for i in range(len(other)))
                                                   for column_i in range(len(other[0]))), self))
        else:
            raise NotImplementedError()

    def __rmul__(self, other):
        raise NotImplementedError()


class Box:
    def __init__(self, *corners):
        corners = [tuple(c) for c in corners]
        self.lower = Vec(*map(min, zip(*corners)))
        self.upper = Vec(*map(max, zip(*corners)))

    @classmethod
    def empty(cls, dim):
        b = cls()
        b.lower = Vec(*(math.inf,) * dim)
        b.upper = Vec(*(-math.inf,) * dim)
        return b

    def __contains__(self, item):
        return all(mi <= i <= ma for mi, ma, i in zip(self.lower, self.upper, item))

    def __repr__(self):
        return f"Box{{{self.lower}...{self.upper}}}"

    def overlaps(self, other):
        return all(sl <= ol <= su or sl <= ou <= su or ol <= sl <= ou or ol <= su <= ou
                   for sl, su, ol, ou in zip(self.lower, self.upper, other.lower, other.upper))

    def is_empty(self):
        return all(sl == math.inf and su == -math.inf for sl, su in zip(self.lower, self.upper))

    def __and__(self, other):
        if isinstance(other, Box):
            if self.overlaps(other):
                return Box(map(max, zip(self.lower, other.lower)), map(min, zip(self.upper, other.upper)))
            else:
                return Box.empty(len(self.lower))
        else:
            raise NotImplementedError()

    def size(self):
        return reduce(operator.mul, map(lambda l, u: u - l + 1, self.lower, self.upper))


def nth(iterable, n):
    return next(islice(iterable, n, None))


# Adapted from https://www.reddit.com/r/adventofcode/comments/rf7onx/2021_day_13_solutions/hocy115/
def ocr(m: set[tuple[int, int]]):
    mx, my = max(x for x, y in m), max(y for x, y in m)
    assert my == 5, "Letters need to be 6 rows high"
    s = ""
    for i in range(0, mx + 1, 5):
        v = int("".join("1" if (i + x, y) in m else "0" for y in range(6) for x in range(4)), 2)
        try:
            s += {6922137: "A", 15329694: "B", 6916246: "C", 16312463: "E", 16312456: "F", 6917015: "G", 10090905: "H",
                  7479847: "I", 3215766: "J", 10144425: "K", 8947855: "L", 6920598: "O", 15310472: "P", 15310505: "R",
                  7898654: "S", 10066326: "U", 8933922: "Y", 15803535: "Z"}[v]
        except KeyError:
            letter = "\n".join("".join("▓" if (i + x, y) in m else " " for x in range(4)) for y in range(6))
            print(f"Unknown Letter with id {v}:\n\n{letter}")
            raise KeyError
    return s


# 2018 10 uses 10-pixel high letters
def ocr10(m: set[tuple[int, int]]):
    mx, my = max(x for x, y in m), max(y for x, y in m)
    assert my == 9, "Letters need to be 10 rows high"
    s = ""
    for i in range(0, mx + 1, 8):
        v = int("".join("1" if (i + x, y) in m else "0" for y in range(10) for x in range(6)), 2)
        try:
            s += {221386771471407201: "A", 1126328852231362686: "B", 549863600932653150: "C", 1144057308981102655: "E",
                  549863601050360029: "G", 603911296530126945: "H", 126672675233474716: "J", 604206430830086305: "K",
                  585610922974906431: "L", 1126328852214319136: "P", 1126328852281960545: "R", 603844239923161185: "X",
                  1135193120993052735: "Z"}[v]
        except KeyError:
            letter = "\n".join("".join("▓" if (i + x, y) in m else " " for x in range(6)) for y in range(10))
            print(f"Unknown Letter with id {v}:\n\n{letter}")
            raise KeyError
    return s


class PriorityQueue:
    def __init__(self):
        self.items = {}
        self.index = 0
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def put(self, item, priority):
        self.items[self.index] = item
        heappush(self.queue, (priority, self.index))
        self.index += 1

    def get(self):
        i = heappop(self.queue)[1]
        item = self.items[i]
        del self.items[i]
        return item


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


def a_star(start, is_goal, get_neighbors, h=lambda s: 0, d=None):
    # h is 0 by default to use Dijkstra if no h is supplied

    if not callable(is_goal):  # if goal is not a lambda, create a simple equals lambda
        goal = is_goal
        is_goal = lambda x: x == goal

    if d is not None:  # if d is not supplied, expect get_neighbors to yield (state, distance)
        get_neighbors_without_distance = get_neighbors
        get_neighbors = lambda s: ((n, d(s, n)) for n in get_neighbors_without_distance(s))

    open_set = PriorityQueue()
    g_score = defaultdict(lambda: math.inf)
    came_from = {}
    seen = set()

    if isinstance(start, dict):  # if start is a dict, it can supply starting distances
        for s, g in start.items():
            g_score[s] = g
    elif isinstance(start, list) or isinstance(start, set):  # if list or set: multiple starts provided
        for s in start:
            g_score[s] = 0
    else:  # otherwise assume single start
        g_score[start] = 0

    for s, g in g_score.items():
        open_set.put(s, g_score[s] + h(s))

    while open_set:
        current = open_set.get()

        if current in seen:
            continue
        seen.add(current)

        if is_goal(current):
            return reconstruct_path(came_from, current), g_score[current]

        for neighbor, distance in get_neighbors(current):
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                open_set.put(neighbor, tentative_g_score + h(neighbor))


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


class IntInterval(portion.AbstractDiscreteInterval):
    _step = 1


portion_integer = portion.create_api(IntInterval)
