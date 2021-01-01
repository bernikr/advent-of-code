import itertools

from aocd import get_data


def part1(a):
    return sum(max(l) - min(l) for l in a)


def part2(a):
    return sum(next(a // b for a, b in itertools.permutations(l, 2) if a % b == 0) for l in a)


if __name__ == '__main__':
    data = get_data(day=2, year=2017)
    inp = [list(map(int, l.split('\t'))) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
