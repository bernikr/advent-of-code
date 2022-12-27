import math
from collections import defaultdict

from aoc_utils import Vec

square = [
    Vec(-1, -1), Vec(0, -1), Vec(1, -1),
    Vec(-1, 0), Vec(0, 0), Vec(1, 0),
    Vec(-1, 1), Vec(0, 1), Vec(1, 1),
]


def enhance(img, alg):
    xmin = min(x for x, _ in img) - 1
    xmax = max(x for x, _ in img) + 1
    ymin = min(y for _, y in img) - 1
    ymax = max(y for _, y in img) + 1
    if img.default_factory():
        default = alg[-1]
    else:
        default = alg[0]
    return defaultdict(lambda: default,
                       {Vec(x, y): alg[int(''.join('1' if img[(Vec(x, y) + c)] else '0' for c in square), 2)]
                        for x in range(xmin, xmax + 1) for y in range(ymin, ymax + 1)})


def part1(inp):
    alg, img = inp
    for _ in range(2):
        img = enhance(img, alg)
    return sum(img.values()) if not img.default_factory() else math.inf


def part2(inp):
    alg, img = inp
    for _ in range(50):
        img = enhance(img, alg)
    return sum(img.values()) if not img.default_factory() else math.inf


def solve(inp, ispart1):
    inp1, inp2 = inp.split('\n\n')
    inp1 = [c == '#' for c in inp1.replace('\n', '')]
    inp2 = defaultdict(lambda: False,
                       {Vec(x, y): c == '#' for y, l in enumerate(inp2.splitlines()) for x, c in enumerate(l)})
    inp = (inp1, inp2)
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
