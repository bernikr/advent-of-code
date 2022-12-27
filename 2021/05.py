import math
import re
from collections import defaultdict

from aoc_utils import Vec


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


def solve(inp, ispart1):
    inp = [(Vec(a, b), Vec(c, d)) for a, b, c, d in
           ((tuple(map(int, a))) for a in
            (re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).groups() for l in inp.splitlines()))]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
