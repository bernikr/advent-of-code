from aocd import get_data
from future.moves import collections


def part1(a):
    return ''.join(max(collections.Counter(c).items(), key=lambda x: x[1])[0] for c in zip(*a))


def part2(a):
    return ''.join(max(collections.Counter(c).items(), key=lambda x: -x[1])[0] for c in zip(*a))


if __name__ == '__main__':
    data = get_data(day=6, year=2016)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
