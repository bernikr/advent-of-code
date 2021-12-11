import math
import operator
from functools import reduce

from aoc_utils import Vec, dirs4
from aocd import get_data


def part1(inp):
    return sum(v + 1 for p, v in inp.items() if v < min(inp.get(p + d, math.inf) for d in dirs4))


def calculate_basin_size(mapp, lowpoint):
    basin = {lowpoint}
    boundary = {lowpoint}
    while boundary:
        nb = set()
        for p in boundary:
            for d in dirs4:
                if (p + d) not in basin and mapp.get(p + d, 9) < 9:
                    basin.add(p + d)
                    nb.add(p + d)
        boundary = nb
    return len(basin)


def part2(inp):
    return reduce(operator.mul,
                  sorted((calculate_basin_size(inp, p)
                          for p in (p for p, v in inp.items() if v < min(inp.get(p + d, math.inf) for d in dirs4))),
                         reverse=True)[:3])


if __name__ == '__main__':
    data = get_data(day=9, year=2021)
    inp = {Vec(x, y): int(n) for y, l in enumerate(data.splitlines()) for x, n in enumerate(l)}
    print(part1(inp))
    print(part2(inp))
