from __future__ import annotations

import re
from itertools import pairwise
from operator import itemgetter

from aoc_utils import Vec
from aocd import data, submit, AocdError
from tqdm import tqdm


def overlaps(a, b):
    return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1] or \
           b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[0]


def union(a, b):
    return min(a[0], b[0]), max(a[1], b[1])


def simplify_line(y, scanners):
    intervals = sorted((a - (r - abs(b - y)), a + (r - abs(b - y))) for (a, b), r in scanners if r >= abs(b - y))
    simplified = [intervals[0]]
    for i in intervals:
        if overlaps(i, simplified[-1]):
            simplified[-1] = union(i, simplified[-1])
        else:
            simplified.append(i)
    return simplified


def solve(inp, part1):
    inp = [tuple(map(lambda x: Vec(*map(int, x)), re.findall(r"x=([\-\d]+), y=([\-\d]+)", l)))
           for l in inp.splitlines()]
    beacons = set(map(itemgetter(1), inp))
    scanners = [(s, (s - b).manhatten()) for s, b in inp]
    if part1:
        return sum(b - a + 1 for (a, b) in simplify_line(2000000, scanners)) \
               - sum(1 for pos in beacons if pos[1] == 2000000)
    else:
        for y in tqdm(range(4000001)):
            simpl = simplify_line(y, scanners)
            if len(simpl) >= 2:
                for (_, a), (b, _) in pairwise(simpl):
                    if a + 2 == b and 0 <= a + 1 <= 4000000:
                        return y + (a + 1) * 4000000


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
