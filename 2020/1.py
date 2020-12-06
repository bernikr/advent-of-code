from itertools import product

from aocd import get_data


def part1(a):
    return next(a * b for a, b in (product((int(l.strip()) for l in a), repeat=2)) if a + b == 2020)


def part2(a):
    return next(a * b * c for a, b, c in (product((int(l.strip()) for l in a), repeat=3)) if a + b + c == 2020)


if __name__ == '__main__':
    data = get_data(day=1, year=2020)
    input = data.splitlines()
    print(part1(input))
    print(part2(input))
