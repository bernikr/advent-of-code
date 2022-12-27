import operator
from collections import defaultdict
from functools import reduce
from itertools import count

from aoc_utils import Vec, dirs4


def is_visible_dir(tree, mapp, dir):
    p = tree
    mapp = defaultdict(lambda: -1, mapp)
    while mapp[p] != -1:
        p += dir
        if mapp[p] >= mapp[tree]:
            return False
    return True


def solve1(inp):
    return sum(1 for t in inp if any(is_visible_dir(t, inp, d) for d in dirs4))


def viewing_distance(tree, mapp, d):
    mapp = defaultdict(lambda: -1, mapp)
    for i in count(1):
        pos = tree + i * d
        if mapp[pos] == -1:
            return i - 1
        if mapp[pos] >= mapp[tree]:
            return i


def solve2(inp):
    return max(reduce(operator.mul, (viewing_distance(t, inp, d) for d in dirs4)) for t in inp)


def solve(inp, part1):
    inp = {Vec(x, y): int(c) for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    return solve1(inp) if part1 else solve2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
