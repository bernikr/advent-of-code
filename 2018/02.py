import itertools
from collections import Counter

from aocd import get_data


def part1(a):
    cs = list(map(Counter, a))
    return sum(2 in c.values() for c in cs) * sum(3 in c.values() for c in cs)


def part2(a):
    return next(''.join(x for x, y in zip(*c) if x == y)
                for c in itertools.combinations(a, 2) if sum(x != y for x, y in zip(*c)) == 1)


if __name__ == '__main__':
    data = get_data(day=2, year=2018)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
