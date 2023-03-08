import re
from functools import cache

from aoc_utils import Vec


@cache
def geo_idx(c, depth, target):
    if c == (0, 0) or c == target:
        return 0
    x, y = c
    if y == 0:
        return x * 16807
    if x == 0:
        return y * 48271
    return ero_lvl(Vec(x - 1, y), depth, target) * ero_lvl(Vec(x, y - 1), depth, target)


@cache
def ero_lvl(c, depth, target):
    return (geo_idx(c, depth, target) + depth) % 20183


def solve(inp, part1):
    depth, x, y = map(int, re.findall(r"\d+", inp))
    target = Vec(x, y)
    if part1:
        return sum(ero_lvl(Vec(x,y), depth, target) % 3 for x in range(target[0]+1) for y in range(target[1]+1))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
