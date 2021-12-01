from itertools import pairwise

from aocd import get_data


def part1(inp):
    return sum(b > a for a, b in pairwise(inp))


def part2(inp):
    return sum(b > a for a, b in zip(inp, inp[3:]))


if __name__ == '__main__':
    data = get_data(day=1, year=2021)
    inp = list(map(int, data.splitlines()))
    print(part1(inp))
    print(part2(inp))
