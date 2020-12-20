from itertools import accumulate

from aocd import get_data


def part1(a):
    return sum(map(lambda x: 1 if x == '(' else -1, a))


def part2(a):
    return next(i + 1 for i, n in enumerate(accumulate(map(lambda x: 1 if x == '(' else -1, a))) if n < 0)


if __name__ == '__main__':
    data = get_data(day=1, year=2015)
    inp = data
    print(part1(inp))
    print(part2(inp))
