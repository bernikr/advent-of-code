from __future__ import annotations

import math
import operator
from collections import UserList, defaultdict
from collections.abc import Callable, Collection, Iterable
from enum import Enum
from functools import reduce
from heapq import heappop, heappush
from itertools import islice, product
from math import sqrt
from typing import Literal, Self

import portion  # type: ignore[import-untyped]


class Vec[T: int | float = int](tuple[T, ...]):
    __slots__ = ()

    def __new__(cls, *args: T | Iterable[T]) -> Self:
        if len(args) == 1 and isinstance(args[0], Iterable):
            return super().__new__(cls, args[0])
        return super().__new__(cls, args)  # type: ignore[arg-type]

    def __add__(self, other: tuple[T, ...]) -> Vec[T]:  # type: ignore[override]
        if self.__len__() == other.__len__() == 2:  # performance optimization for 2D vectors
            return tuple.__new__(Vec, (self[0] + other[0], self[1] + other[1]))  # type: ignore[operator]
        if len(self) != len(other):
            msg = "Adding vectors of different dimensions is not supported"
            raise ValueError(msg)
        return Vec(map(operator.add, self, other))

    def __sub__(self, other: tuple[float, ...]) -> Vec[T]:
        if len(self) != len(other):
            msg = "Subtracting vectors of different dimensions is not supported"
            raise ValueError(msg)
        return Vec(map(operator.sub, self, other))

    def __mul__(self, other: T) -> Vec[T]:  # type: ignore[override]
        if isinstance(other, int | float):
            return Vec(x * other for x in self)  # type: ignore[misc, operator]
        raise NotImplementedError

    def __rmul__(self, other: T) -> Vec[T]:  # type: ignore[override]
        if isinstance(other, int | float):
            return Vec(x * other for x in self)  # type: ignore[misc, operator]
        raise NotImplementedError

    def __truediv__(self, other: float) -> Vec[float]:
        if isinstance(other, int):
            return Vec(x // other if x % other == 0 else x / other for x in self)
        if isinstance(other, float):
            return Vec(x / other for x in self)
        raise NotImplementedError

    def __abs__(self) -> float:
        return sqrt(sum(x * x for x in self))  # type: ignore[misc, operator]

    def pos_mod(self, other: int | Vec[int]) -> Vec[int]:
        if isinstance(other, int):
            other = Vec((other,) * len(self))
        if isinstance(other, Vec):
            if len(self) != len(other):
                msg = "Modulo of vectors of different dimensions is not supported"
                raise ValueError(msg)
            return Vec(map(lambda s, o: (s % o + o) % o, self, other))  # type: ignore[return-value, arg-type]
        raise NotImplementedError

    def manhatten(self) -> T:
        return sum(abs(x) for x in self)  # type: ignore[misc, return-value]

    def turn_left(self) -> Vec[T]:
        if len(self) != 2:
            msg = "Turning left is only defined for 2D vectors"
            raise ValueError(msg)
        return Vec(self[1], -self[0])

    def turn_right(self) -> Vec[T]:
        if len(self) != 2:
            msg = "Turning right is only defined for 2D vectors"
            raise ValueError(msg)
        return Vec(-self[1], self[0])  # type: ignore[arg-type]

    @property
    def x(self) -> T:
        return self[0]

    @property
    def y(self) -> T:
        return self[1]

    @property
    def z(self) -> T:
        return self[2]

    def distance_squared(self) -> T:
        return sum(x * x for x in self)  # type: ignore[misc, return-value, operator]


def create_map(inp: str) -> dict[Vec, str]:
    return {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}


UP = Vec(0, -1)
DOWN = Vec(0, 1)
LEFT = Vec(-1, 0)
RIGHT = Vec(1, 0)

dirs4 = [UP, DOWN, LEFT, RIGHT]
dirs8 = [Vec(*c) for c in product([-1, 0, 1], repeat=2) if c != (0, 0)]


class Dir(Enum):
    UP = UP
    DOWN = DOWN
    LEFT = LEFT
    RIGHT = RIGHT

    def turn_left(self) -> Dir:
        return Dir((self.value[1], -self.value[0]))

    def turn_right(self) -> Dir:
        return Dir((-self.value[1], self.value[0]))


class Matrix(tuple[tuple[int, ...], ...]):
    __slots__ = ()

    def __new__(cls, *args: tuple[int, ...] | Iterable[tuple[int, ...]]) -> Self:
        if len(args) == 1 and isinstance(args[0], Iterable):
            return super().__new__(cls, args[0])  # type: ignore[arg-type]
        return super().__new__(cls, args)  # type: ignore[arg-type]

    def __add__(self, other: Matrix) -> Matrix:  # type: ignore[override]
        raise NotImplementedError

    def __mul__[T: Vec | Matrix](self, other: T) -> T:  # type: ignore[override]
        if isinstance(other, Vec):
            return Vec(sum(a * b for a, b in zip(row, other)) for row in self)  # type: ignore[return-value]
        if isinstance(other, Matrix):
            if len(self[0]) != len(other):
                msg = "Matrix dimensions do not match"
                raise ValueError(msg)
            return Matrix(
                tuple(
                    sum(s_row[i] * other[i][column_i] for i in range(len(other))) for column_i in range(len(other[0]))
                )
                for s_row in self
            )  # type: ignore[return-value]
        raise NotImplementedError

    def __rmul__(self, other: Matrix) -> Matrix:  # type: ignore[override]
        raise NotImplementedError


class Box:
    def __init__(self, *corners: Iterable[float]) -> None:
        corners = [tuple(c) for c in corners]
        self.lower = Vec(*map(min, zip(*corners)))
        self.upper = Vec(*map(max, zip(*corners)))

    @classmethod
    def empty(cls, dim: int) -> Box:
        b = cls()
        b.lower = Vec(*(math.inf,) * dim)
        b.upper = Vec(*(-math.inf,) * dim)
        return b

    def __contains__(self, item: Iterable[float]) -> bool:
        return all(mi <= i <= ma for mi, ma, i in zip(self.lower, self.upper, item))

    def __repr__(self) -> str:
        return f"Box{{{self.lower}...{self.upper}}}"

    def overlaps(self, other: Box) -> bool:
        return all(
            sl <= ol <= su or sl <= ou <= su or ol <= sl <= ou or ol <= su <= ou
            for sl, su, ol, ou in zip(self.lower, self.upper, other.lower, other.upper)
        )

    def is_empty(self) -> bool:
        return all(sl == math.inf and su == -math.inf for sl, su in zip(self.lower, self.upper))

    def __and__(self, other: Box) -> Box:
        if isinstance(other, Box):
            if self.overlaps(other):
                return Box(map(max, zip(self.lower, other.lower)), map(min, zip(self.upper, other.upper)))
            return Box.empty(len(self.lower))
        raise NotImplementedError

    def size(self) -> float:
        return reduce(operator.mul, map(lambda l, u: u - l + 1, self.lower, self.upper))  # type: ignore[no-any-return]


def nth[T](iterable: Iterable[T], n: int) -> T:
    return next(islice(iterable, n, None))


# Adapted from https://www.reddit.com/r/adventofcode/comments/rf7onx/2021_day_13_solutions/hocy115/
def ocr(m: set[tuple[int, int]]) -> str:
    mx, my = max(x for x, y in m), max(y for x, y in m)
    if my != 5:
        msg = "Letters need to be 6 rows high"
        raise ValueError(msg)
    s = ""
    for i in range(0, mx + 1, 5):
        v = int("".join("1" if (i + x, y) in m else "0" for y in range(6) for x in range(4)), 2)
        try:
            s += {
                6922137: "A",
                15329694: "B",
                6916246: "C",
                16312463: "E",
                16312456: "F",
                6917015: "G",
                10090905: "H",
                7479847: "I",
                3215766: "J",
                10144425: "K",
                8947855: "L",
                6920598: "O",
                15310472: "P",
                15310505: "R",
                7898654: "S",
                10066326: "U",
                8933922: "Y",
                15803535: "Z",
            }[v]
        except KeyError as e:
            letter = "\n".join("".join("▓" if (i + x, y) in m else " " for x in range(4)) for y in range(6))
            print(f"Unknown Letter with id {v}:\n\n{letter}")
            raise KeyError from e
    return s


# 2018 10 uses 10-pixel high letters
def ocr10(m: set[tuple[int, int]]) -> str:
    mx, my = max(x for x, y in m), max(y for x, y in m)
    if my != 9:
        msg = "Letters need to be 10 rows high"
        raise ValueError(msg)
    s = ""
    for i in range(0, mx + 1, 8):
        v = int("".join("1" if (i + x, y) in m else "0" for y in range(10) for x in range(6)), 2)
        try:
            s += {
                221386771471407201: "A",
                1126328852231362686: "B",
                549863600932653150: "C",
                1144057308981102655: "E",
                549863601050360029: "G",
                603911296530126945: "H",
                126672675233474716: "J",
                604206430830086305: "K",
                585610922974906431: "L",
                1126328852214319136: "P",
                1126328852281960545: "R",
                603844239923161185: "X",
                1135193120993052735: "Z",
            }[v]
        except KeyError as e:
            letter = "\n".join("".join("▓" if (i + x, y) in m else " " for x in range(6)) for y in range(10))
            print(f"Unknown Letter with id {v}:\n\n{letter}")
            raise KeyError from e
    return s


class PriorityQueue[T]:
    def __init__(self) -> None:
        self.items: dict[int, T] = {}
        self.index: int = 0
        self.queue: list[tuple[float, int]] = []

    def __len__(self) -> int:
        return len(self.queue)

    def put(self, item: T, priority: float) -> None:
        self.items[self.index] = item
        heappush(self.queue, (priority, self.index))
        self.index += 1

    def get(self) -> T:
        i = heappop(self.queue)[1]
        item = self.items[i]
        del self.items[i]
        return item


def reconstruct_path[T](predecessors: dict[T, T], current: T) -> list[T]:
    path = [current]
    while current in predecessors:
        current = predecessors[current]
        path.append(current)
    return path[::-1]


def reconstruct_paths[T](predecessors: dict[T, Collection[T]], goal: T) -> Iterable[list[T]]:
    linear_path = reconstruct_path({k: next(iter(v)) for k, v in predecessors.items() if len(v) == 1}, goal)
    new_goal = linear_path[0]
    if new_goal not in predecessors or len(predecessors[new_goal]) == 0:
        yield linear_path
    else:
        for pre in predecessors[new_goal]:
            yield from ([*path, *linear_path] for path in reconstruct_paths(predecessors, pre))


def a_star[T](  # noqa: C901, PLR0912
    start: T | dict[T, float] | list[T] | set[T],
    is_goal: T | Callable[[T], bool],
    get_neighbors: Callable[[T], Iterable[T | tuple[T, float]]],
    h: Callable[[T], float] = lambda _: 0,  # h is 0 by default to use Dijkstra if no h is supplied
    d: Callable[[T, T], float] | None = None,
) -> tuple[dict[T, set[T]], float]:
    if not callable(is_goal):  # if goal is not a lambda, create a simple equals lambda
        goal = is_goal
        is_goal = lambda x: x == goal

    if d is not None:  # if d is not supplied, expect get_neighbors to yield (state, distance)
        get_neighbors_without_distance = get_neighbors
        get_neighbors = lambda x: ((n, d(x, n)) for n in get_neighbors_without_distance(x))  # type: ignore[misc, arg-type]

    open_set = PriorityQueue[T]()
    g_score = defaultdict[T, float](lambda: math.inf)
    predecessors = defaultdict[T, set[T]](set)
    seen = set()

    if isinstance(start, dict):  # if start is a dict, it can supply starting distances
        for s, g in start.items():
            g_score[s] = g
    elif isinstance(start, list | set):  # if list or set: multiple starts provided
        for s in start:
            g_score[s] = 0
    else:  # otherwise assume single start
        g_score[start] = 0

    for s, g in g_score.items():
        open_set.put(s, g + h(s))

    while open_set:
        current = open_set.get()

        if current in seen:
            continue
        seen.add(current)

        if is_goal(current):
            return dict(predecessors), g_score[current]

        for neighbor, distance in get_neighbors(current):  # type: ignore[misc]
            tentative_g_score = g_score[current] + distance
            if tentative_g_score <= g_score[neighbor]:
                predecessors[neighbor].add(current)
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                open_set.put(neighbor, tentative_g_score + h(neighbor))
    msg = "No path found"
    raise ValueError(msg)


class CircularList[T](UserList[T]):
    def __getitem__(self, key: int | slice) -> T | list[T]:  # type: ignore[override]
        if isinstance(key, int):
            return super().__getitem__(key % len(self))
        if isinstance(key, slice):
            return [
                self[i]  # type: ignore[misc]
                for i in range(
                    key.start if key.start is not None else 0,
                    key.stop if key.stop is not None else len(self),
                    key.step if key.step is not None else 1,
                )
            ]
        raise NotImplementedError

    def __setitem__(self, key: int | slice, value: T | list[T]) -> None:  # type: ignore[override]
        if isinstance(key, int):
            super().__setitem__(key % len(self), value)  # type: ignore[assignment]
        elif isinstance(key, slice):
            keys = list(
                range(
                    key.start if key.start is not None else 0,
                    key.stop if key.stop is not None else len(self),
                    key.step if key.step is not None else 1,
                ),
            )
            if len(keys) != len(value):  # type: ignore[arg-type]
                msg = "CircularList: Replacing slices of different length is currently not implemented"
                raise NotImplementedError(msg)
            for k, v in zip(keys, value):  # type: ignore[arg-type]
                self[k] = v
        else:
            raise NotImplementedError


def sign(x: float) -> Literal[0, 1, -1]:
    return x and (1, -1)[x < 0]  # type: ignore[return-value]


class IntInterval(portion.AbstractDiscreteInterval):  # type: ignore[misc]
    _step = 1


portion_integer = portion.create_api(IntInterval)


# helpers for typechecking tuples
def tuple2[T](x: Iterable[T]) -> tuple[T, T]:
    x = tuple(x)
    if len(x) != 2:
        msg = "Expected a tuple of length 2"
        raise ValueError(msg)
    return x


def tuple3[T](x: Iterable[T]) -> tuple[T, T, T]:
    x = tuple(x)
    if len(x) != 3:
        msg = "Expected a tuple of length 3"
        raise ValueError(msg)
    return x
