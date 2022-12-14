from itertools import pairwise, count

from aoc_utils import Vec, sign
from aocd import data, submit, AocdError


def drop_sand_unit(pos, mapp, lim):
    candidates = [Vec(0, 1), Vec(-1, 1), Vec(1, 1), None]
    while pos[1] < lim:
        for dir in candidates:
            if dir is None:
                return pos
            if pos + dir not in mapp:
                pos += dir
                break
    return pos


def solve(inp, part1):
    mapp = set()
    for path in inp.splitlines():
        for a, b in pairwise(Vec(*map(int, c.split(','))) for c in path.split(' -> ')):
            dir = Vec(*map(sign, b - a))
            p = a
            mapp.add(p)
            while p != b:
                p += dir
                mapp.add(p)
    lim = 1 + max(map(lambda x: x[1], mapp))
    for i in count():
        new_pos = drop_sand_unit(Vec(500, 0), mapp, lim)
        if part1 and new_pos[1] == lim:
            return i
        if not part1 and new_pos == Vec(500, 0):
            return i + 1
        mapp.add(new_pos)


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
