import itertools
import re
from collections import defaultdict
from functools import reduce

from aocd import get_data


def process_claims(cs):
    r = defaultdict(list)
    for c in cs:
        for i in range(c[1], c[1] + c[3]):
            for j in range(c[2], c[2] + c[4]):
                r[(i, j)].append(c[0])
    return r


def part1(a):
    return sum(len(cs) >= 2 for cs in a.values())


def part2(a):
    return (set(itertools.chain.from_iterable(a.values()))
            - reduce(set.union, (set(x) for x in a.values() if len(x) >= 2))).pop()


if __name__ == '__main__':
    data = get_data(day=3, year=2018)
    inp = process_claims(tuple(map(int, re.match(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$", l).groups()))
                         for l in data.splitlines())
    print(part1(inp))
    print(part2(inp))
