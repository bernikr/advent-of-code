import math
import re
from collections import defaultdict
from functools import cache

from aoc_utils import Box, Vec

DOWN = Vec(0, 0, -1)


@cache
def settle_bricks(inp):
    falling = sorted([Box((x1, y1, z1), (x2, y2, z2)) for x1, y1, z1, x2, y2, z2 in
                      (tuple(map(int, re.findall(r"\d+", l))) for l in inp.splitlines())], key=lambda b: b.lower[2])
    ground = Box((0, 0, 0), (math.inf, math.inf, 0))
    settled = defaultdict(list)
    settled[0].append((0, ground))
    settled_next_i = 1
    supported_by = defaultdict(list)
    while falling:
        settled_changed = False
        new_falling = []
        for b in falling:
            b.lower += DOWN
            b.upper += DOWN
            for i, other in settled[b.lower[2]]:
                if b.overlaps(other):
                    supported_by[settled_next_i].append(i)
            b.lower -= DOWN
            b.upper -= DOWN
            if supported_by[settled_next_i]:
                settled[b.upper[2]].append((settled_next_i, b))
                settled_next_i += 1
                settled_changed = True
            else:
                new_falling.append(b)
        falling = new_falling
        if not settled_changed:
            for b in falling:
                b.lower += DOWN
                b.upper += DOWN
    return supported_by


def calculate_fallen(supported_by, supports, disintegrate):
    supported_by = {a: list(b) for a, b in supported_by.items()}
    fallen = 0
    to_destroy = {disintegrate}
    while to_destroy:
        b = to_destroy.pop()
        for i in supports[b]:
            supported_by[i].remove(b)
            if not supported_by[i]:
                fallen += 1
                to_destroy.add(i)
    return fallen


def solve(inp, part1):
    supported_by = settle_bricks(inp)
    supports = defaultdict(list)
    for i, l in supported_by.items():
        for j in l:
            supports[j].append(i)
    if part1:
        return sum(calculate_fallen(supported_by, supports, i) == 0 for i in range(1, len(supported_by) + 1))
    else:
        return sum(calculate_fallen(supported_by, supports, i) for i in range(1, len(supported_by) + 1))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
