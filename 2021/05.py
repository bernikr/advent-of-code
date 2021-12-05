import math
import re
from collections import defaultdict

from aoc_utils import Vec
from aocd import get_data


def simplify(c):
    return c / math.gcd(*c)


def count_overlaps(inp, include_diagonals):
    lines_per_point = defaultdict(lambda: 0)
    for start, end in inp:
        d = simplify(end - start)
        if all(c != 0 for c in d) and not include_diagonals:
            continue
        lines_per_point[start] += 1
        pos = start
        while pos != end:
            pos += d
            lines_per_point[pos] += 1
    return sum(n >= 2 for n in lines_per_point.values())


def part1(inp):
    return count_overlaps(inp, False)


def part2(inp):
    return count_overlaps(inp, True)


if __name__ == '__main__':
    data = get_data(day=5, year=2021)
    inp = [(Vec(a, b), Vec(c, d)) for a, b, c, d in
           ((tuple(map(int, a))) for a in
            (re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).groups() for l in data.splitlines()))]
    print(part1(inp))
    print(part2(inp))
