from functools import reduce
from operator import itemgetter, or_

from aoc_utils import Vec


# todo: this is inefficient (maybe there are faster solutions by doing it rowwise, spliting and sorting)
def slide(rocks, walls, d):
    for r in rocks.copy():
        rocks.remove(r)
        while True:
            tr = r + d
            while tr in rocks:
                tr += d
            if tr in walls:
                break
            r = tr
        rocks.add(r)
    return rocks


def solve(inp, part1):
    inp = {Vec(x, y): c for y, l in enumerate(reversed(inp.splitlines()), 1) for x, c in enumerate(l, 1)}  # y flip
    rocks = {p for p, c in inp.items() if c == "O"}
    xmax, ymax = map(max, zip(*inp.keys()))
    walls = {p for p, c in inp.items() if c == "#"}
    walls |= reduce(or_, ({Vec(x, 0), Vec(x, ymax + 1)} for x in range(xmax + 1)))
    walls |= reduce(or_, ({Vec(0, y), Vec(xmax + 1, y)} for y in range(ymax + 1)))
    if part1:
        rocks = slide(rocks, walls, Vec(0, 1))
    else:
        seen = {}
        i = 1000000000
        shortcut = False
        while i > 0:
            i -= 1
            for d in [Vec(0, 1), Vec(-1, 0), Vec(0, -1), Vec(1, 0)]:
                rocks = slide(rocks, walls, d)
            if not shortcut:
                r = frozenset(rocks)
                if r in seen:
                    cycle_length = seen[r] - i
                    i = i % cycle_length
                    shortcut = True
                seen[r] = i
    return sum(map(itemgetter(1), rocks))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
