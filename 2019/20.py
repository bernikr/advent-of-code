import operator
from enum import Enum
from functools import cache
from itertools import count
from operator import itemgetter

from aocd import get_data


# https://stackoverflow.com/a/49778990
class DefaultDict(dict):
    def __init__(self, default, d=None, **kwargs):
        super().__init__(**kwargs)
        self.default = default
        if d is not None:
            for k, v in d.items():
                self[k] = v

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.default

    def __hash__(self):
        return id(self)


class Dir(Enum):
    UP = (0, -1, 0)
    DOWN = (0, 1, 0)
    LEFT = (-1, 0, 0)
    RIGHT = (1, 0, 0)

    def move(self, c):
        return add_coords(c, self.value)


def add_coords(a: tuple, b: tuple) -> tuple:
    return tuple(map(operator.add, a, b))


def all_locations(mapp):
    return ((x, y) for x in range(max(map(itemgetter(0), mapp)) + 1) for y in range(max(map(itemgetter(1), mapp)) + 1))


@cache
def find_label(mapp, label) -> list[tuple[int, int]]:
    return list(map(lambda c: next(add_coords(c, d) for d in [(2, 0), (0, 2), (-1, 0), (0, -1)]
                                   if mapp[add_coords(c, d)[:2]] == '.'),
                    (c for c in all_locations(mapp) if mapp[c] == label[0] and
                     any(mapp[d.move(c)[:2]] == label[1]
                         for d in [Dir.RIGHT, Dir.DOWN]))))


def get_label_for(mapp, c: tuple[int, int]) -> str:
    d = next(d for d in Dir if 'A' <= mapp[d.move(c)[:2]] <= 'Z')
    first = mapp[d.move(c)[:2]]
    second = mapp[d.move(d.move(c))[:2]]
    if d in [Dir.LEFT, Dir.UP]:
        first, second = second, first
    return first + second


def inside_label(mapp, c: tuple[int, int]) -> bool:
    size = (max(map(itemgetter(0), mapp)), max(map(itemgetter(1), mapp)))
    return min(*c[:2], *map(operator.sub, size, c)) > 4


def part1(inp):
    mapp = DefaultDict(' ', inp)
    boundary = {find_label(mapp, "AA")[0]}
    visited = boundary.copy()
    for i in count():
        nb = set()
        for c in boundary:
            for d in Dir:
                match mapp[d.move(c)]:
                    case '.':
                        if d.move(c) not in visited:
                            nb.add(d.move(c))
                    case x if x == 'Z' and get_label_for(mapp, c) == 'ZZ':
                        return i
                    case x if 'A' <= x <= 'Z' and get_label_for(mapp, c) != 'AA':
                        l = get_label_for(mapp, c)
                        nc = next(nc for nc in find_label(mapp, l) if nc != c)
                        if nc not in visited:
                            nb.add(nc)
        boundary = nb
        visited = visited.union(nb)


def part2(inp):
    mapp = DefaultDict(' ', inp)
    boundary = {(*find_label(mapp, "AA")[0], 0)}
    visited = boundary.copy()
    for i in count():
        nb = set()
        for c in boundary:
            for d in Dir:
                match mapp[d.move(c)[:2]]:
                    case '.':
                        if d.move(c) not in visited:
                            nb.add(d.move(c))
                    case x if x == 'Z' and get_label_for(mapp, c) == 'ZZ' and c[2] == 0:
                        return i
                    case x if 'A' <= x <= 'Z' and get_label_for(mapp, c) not in ['AA', 'ZZ']:
                        l = get_label_for(mapp, c)
                        depth = c[2] + (1 if inside_label(mapp, c) else -1)
                        if depth >= 0:
                            nc = (*next(nc for nc in find_label(mapp, l) if nc != c[:2]), depth)
                            if nc not in visited:
                                nb.add(nc)
        boundary = nb
        visited = visited.union(nb)


if __name__ == '__main__':
    data = get_data(day=20, year=2019)
    inp = {(x, y): c for y, l in enumerate(data.splitlines()) for x, c in enumerate(l)}
    print(part1(inp))
    print(part2(inp))
