import itertools
import re
from collections import defaultdict
from functools import reduce


def process_claims(cs):
    r = defaultdict(list)
    for c in cs:
        for i in range(c[1], c[1] + c[3]):
            for j in range(c[2], c[2] + c[4]):
                r[(i, j)].append(c[0])
    return r


def part1(a):
    return sum(len(cs) >= 2 for cs in a.values())


def part2(a):
    return (set(itertools.chain.from_iterable(a.values()))
            - reduce(set.union, (set(x) for x in a.values() if len(x) >= 2))).pop()


def solve(inp, ispart1):
    inp = process_claims(tuple(map(int, re.match(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$", l).groups()))
                         for l in inp.splitlines())
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
