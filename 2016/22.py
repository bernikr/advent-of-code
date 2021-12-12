import re
from itertools import product, chain

from aoc_utils import Vec, dirs4
from aocd import get_data


def part1(inp):
    return sum(c1 != c2 and u1 != 0 and u1 <= a2 for (c1, (u1, a1)), (c2, (u2, a2)) in product(inp.items(), repeat=2))


def part2(inp):
    mapp = inp.copy()
    available_moves = list(chain.from_iterable(((c, c+d) for d in dirs4 if mapp.get(c + d, (0, -1))[1] >= u > 0)
                                               for c, (u, a) in mapp.items()))
    return available_moves


if __name__ == '__main__':
    data = get_data(day=22, year=2016)
    inp = {Vec(x, y): (u, a) for x, y, u, a in
           (tuple(map(int, re.match(r'^/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+%$', l).groups()))
            for l in data.splitlines()[2:])}
    print(part1(inp))
    print(part2(inp))
