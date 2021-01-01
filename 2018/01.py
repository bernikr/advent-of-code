import itertools
from itertools import accumulate

from aocd import get_data


def part1(a):
    return sum(a)


def part2(a):
    seen = set()
    f = 0
    for i in itertools.cycle(a):
        if f in seen:
            return f
        seen.add(f)
        f += i


if __name__ == '__main__':
    data = get_data(day=1, year=2018)
    inp = list(map(int, data.splitlines()))
    print(part1(inp))
    print(part2(inp))
