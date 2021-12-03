import math
from itertools import groupby, chain
from operator import itemgetter

from aocd import get_data


def simplify(a, b):
    if b == 0:
        return (-1, 0) if a < 0 else (1, 0)
    elif a == 0:
        return (0, -1) if b < 0 else (0, 1)
    gcd = math.gcd(a, b)
    return a // gcd, b // gcd


def part1(a):
    return max(len(set(simplify(x - base[0], y - base[1]) for x, y in a if (x, y) != base)) for base in a)


def angle(x, y):
    deg = math.degrees(math.atan2(y, x))
    deg -= 270
    while deg < 0:
        deg += 360
    return deg


def part2(a):
    base = max(a, key=lambda b: len(set(simplify(x - b[0], y - b[1]) for x, y in a if (x, y) != b)))
    astroids = groupby(sorted((simplify(x - base[0], y - base[1]), (x - base[0], y - base[1]))
                              for x, y in a if (x, y) != base), key=itemgetter(0))
    ast = list(map(lambda x: (x[1][0] + base[0], x[1][1] + base[1]),
                   sorted(chain.from_iterable(
                       enumerate(sorted((c[1] for c in cs), key=lambda x: (abs(x[0]), abs(x[1]))))
                       for s, cs in astroids), key=lambda x: (x[0], angle(*x[1])))))
    ast = ast[199]
    return ast[0] * 100 + ast[1]


if __name__ == '__main__':
    data = get_data(day=10, year=2019)
    inp = [(x, y) for y, l in enumerate(data.splitlines()) for x, c in enumerate(l) if c == '#']
    print(part1(inp))
    print(part2(inp))