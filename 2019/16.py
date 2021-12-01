import math
import operator
from functools import reduce, cache
from itertools import chain, repeat, cycle, takewhile, product

from aocd import get_data

base_pattern = [0, 1, 0, -1]


def get_pattern(index):
    return list(chain.from_iterable(repeat(e, index + 1) for e in base_pattern))[1:] + [base_pattern[0]]


def apply_pattern(inp, pattern):
    return abs(sum(a * b for a, b in zip(inp, cycle(pattern)))) % 10


def phase(inp):
    return [apply_pattern(inp, get_pattern(i)) for i in range(len(inp))]


def part1(inp):
    return ''.join(map(str, reduce(lambda x, _: phase(x), range(100), inp)[:8]))


def part2(inp):
    return None


if __name__ == '__main__':
    data = get_data(day=16, year=2019)
    inp = list(map(int, data))
    print(part1(inp))
    print(part2(inp))
