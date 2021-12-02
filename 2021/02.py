import operator
from functools import reduce
from itertools import accumulate

from aocd import get_data

dirs = {
    "forward": (1, 0),
    "down": (0, 1),
    "up": (0, -1),
}


def part1(inp):
    return reduce(operator.mul, reduce(lambda a, b: tuple(map(operator.add, a, b)),
                                       (tuple(map(lambda x: x * n, dirs[d])) for d, n in inp)))


def part2(inp):
    return reduce(operator.mul,
                  reduce(lambda a, b: tuple(map(operator.add, a, b)),
                         map(lambda x: (x[1], x[0] * x[1]),
                             zip(accumulate(dirs[d][1] * n for d, n in inp), (dirs[d][0] * n for d, n in inp)))))


if __name__ == '__main__':
    data = get_data(day=2, year=2021)
    inp = [(l.split(' ')[0], int(l.split(' ')[1])) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
