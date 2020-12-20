import itertools
import re

from aocd import get_data


def part1(a):
    return min(sum(a[1][(r[i], r[i + 1])] for i in range(len(r) - 1)) for r in itertools.permutations(a[0]))


def part2(a):
    return max(sum(a[1][(r[i], r[i + 1])] for i in range(len(r) - 1)) for r in itertools.permutations(a[0]))


if __name__ == '__main__':
    data = get_data(day=9, year=2015)
    data = [re.match(r"^(\w+) to (\w+) = (\d+)$", l).groups() for l in data.splitlines()]
    inp = (set(itertools.chain.from_iterable((a, b) for a, b, _ in data)),
           dict(itertools.chain.from_iterable((((a, b), int(c)), ((b, a), int(c))) for a, b, c in data)))
    print(part1(inp))
    print(part2(inp))
