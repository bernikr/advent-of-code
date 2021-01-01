import itertools

from aocd import get_data


def part1(a):
    return sum(len(l) == len(set(l)) for l in a)


def part2(a):
    return sum(not any(sorted(a) == sorted(b) for a, b in itertools.combinations(l, 2)) for l in a)


if __name__ == '__main__':
    data = get_data(day=4, year=2017)
    inp = [l.split(' ') for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
