import itertools
import re

from aocd import get_data


def is_triangle(t):
    t = sorted(t)
    return t[0] + t[1] > t[2]


def part1(a):
    return sum(is_triangle(t) for t in a)


def part2(a):
    return sum(is_triangle(t) for t in (list(itertools.chain(*zip(*a)))[i:i + 3] for i in range(0, len(a) * 3, 3)))


if __name__ == '__main__':
    data = get_data(day=3, year=2016)
    inp = [tuple(map(int, re.findall(r"\d+", l))) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
