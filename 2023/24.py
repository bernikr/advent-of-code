import re
from itertools import combinations

import sympy as sp

from aoc_utils import Vec, Box


def intersect_paths(paths):
    (p1, d1), (p2, d2) = paths
    if d1[0] * d2[1] - d1[1] * d2[0] == 0:  # if cross-product is 0, paths are parallel
        return None
    # (x,y) = p1 + t1 * d1 = p2 + t2 * d2
    # t1 = (p2.x + t2 * d2.x - p1.x) / d1.x
    # p1.y + (p2.x + t2 * d2.x - p1.x) / d1.x * d1.y = p2.y + t2 * d2.y
    # t2 * d2.y = p1.y + (p2.x + t2 * d2.x - p1.x) / d1.x * d1.y - p2.y
    # t2 * d2.y = p1.y + (p2.x - p1.x) / d1.x * d1.y - p2.y + t2 * d2.x / d1.x * d1.y
    # t2 * d2.y - t2 * d2.x / d1.x * d1.y = p1.y + (p2.x - p1.x) / d1.x * d1.y - p2.y
    # t2 * (d2.y - d2.x / d1.x * d1.y) = p1.y + (p2.x - p1.x) / d1.x * d1.y - p2.y
    # t2 = (p1.y + (p2.x - p1.x) / d1.x * d1.y - p2.y) / (d2.y - d2.x / d1.x * d1.y)
    t2 = (p1[1] + (p2[0] - p1[0]) / d1[0] * d1[1] - p2[1]) / (d2[1] - d2[0] / d1[0] * d1[1])
    t1 = (p2[1] + (p1[0] - p2[0]) / d2[0] * d2[1] - p1[1]) / (d1[1] - d1[0] / d2[0] * d2[1])
    if t1 < 0 or t2 < 0:  # ignore intersections before starting point
        return None
    return p1 + t1 * d1


def solve(inp, part1):
    stones = [(Vec(a, b, c), Vec(d, e, f)) for a, b, c, d, e, f in
              (map(int, re.findall(r"-?\d+", l)) for l in inp.splitlines())]
    if part1:
        stones2d = [(Vec(a, b), Vec(c, d)) for (a, b, _), (c, d, _) in stones]
        test_area = Box((200000000000000,) * 2, (400000000000000,) * 2)
        return sum(p is not None and p in test_area for p in map(intersect_paths, combinations(stones2d, 2)))
    else:
        pos = sp.symarray("pos", 3)
        dir = sp.symarray("dir", 3)
        t = sp.symarray("t", 3)
        equations = []
        for i, (stone_pos, stone_dir) in enumerate(stones[:3]):
            for d in range(3):
                equations.append(sp.Eq(pos[d] + t[i] * dir[d], stone_pos[d] + t[i] * stone_dir[d]))
        res = sp.solve(equations)
        return sum(int(res[0][n]) for n in pos)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
