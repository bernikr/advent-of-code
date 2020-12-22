import itertools
import operator
from functools import reduce

from aocd import get_data


def part1(a):
    group_size = sum(a)//3
    return next(reduce(operator.mul, x)
                for x in itertools.chain.from_iterable(itertools.combinations(a, i)
                                                       for i in range(len(a))) if sum(x) == group_size)


def part2(a):
    group_size = sum(a)//4
    return next(reduce(operator.mul, x)
                for x in itertools.chain.from_iterable(itertools.combinations(a, i)
                                                       for i in range(len(a))) if sum(x) == group_size)


if __name__ == '__main__':
    data = get_data(day=24, year=2015)
    inp = list(map(int, data.splitlines()))
    print(part1(inp))
    print(part2(inp))
