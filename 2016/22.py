import re
from itertools import product, count

from aoc_utils import Vec, dirs4
from aocd import get_data


def part1(inp):
    return sum(c1 != c2 and u1 != 0 and u1 <= a2 for (c1, (u1, a1)), (c2, (u2, a2)) in product(inp.items(), repeat=2))


def part2(inp):
    mapp = inp.copy()
    hole, holecap = next((c, a) for c, (u, a) in mapp.items() if u == 0)
    boundary = {(hole, Vec(max(x for x, y in mapp if y == 0), 0))}
    visited = boundary.copy()
    for i in count(1):
        nb = set()
        for h, t in boundary:
            for d in dirs4:
                if h == (0, 0) and t == h + d:
                    return i
                if mapp.get(h + d, (holecap + 1, 0))[0] <= holecap:
                    if h + d == t:
                        ns = (h + d, h)
                    else:
                        ns = (h + d, t)
                    if ns not in visited:
                        nb.add(ns)
                        visited.add(ns)
        boundary = nb


if __name__ == '__main__':
    data = get_data(day=22, year=2016)
    inp = {Vec(x, y): (u, a) for x, y, u, a in
           (tuple(map(int, re.match(r'^/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+%$', l).groups()))
            for l in data.splitlines()[2:])}
    print(part1(inp))
    print(part2(inp))
