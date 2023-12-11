from itertools import combinations
from operator import itemgetter

from aoc_utils import Vec


def solve(inp, part1):
    stars = {Vec(x, y) for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l) if c == "#"}
    expansion = 1 if part1 else 1000000 - 1
    for i in reversed(range(max(map(itemgetter(0), stars)))):
        if not any(s[0] == i for s in stars):
            stars = {s + Vec(expansion, 0) if s[0] > i else s for s in stars}
    for i in reversed(range(max(map(itemgetter(1), stars)))):
        if not any(s[1] == i for s in stars):
            stars = {s + Vec(0, expansion) if s[1] > i else s for s in stars}
    return sum((a - b).manhatten() for a, b in combinations(stars, 2))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
