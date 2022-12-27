import operator
from functools import reduce
from itertools import accumulate

from aoc_utils import Vec

dirs = {
    "forward": Vec(1, 0),
    "down": Vec(0, 1),
    "up": Vec(0, -1),
}


def part1(inp):
    return reduce(operator.mul, reduce(lambda a, b: tuple(map(operator.add, a, b)),
                                       (dirs[d] * n for d, n in inp)))


def part2(inp):
    return reduce(operator.mul,
                  reduce(operator.add,
                         map(lambda x: Vec(x[1], x[0] * x[1]),
                             zip(accumulate(dirs[d][1] * n for d, n in inp), (dirs[d][0] * n for d, n in inp)))))


def solve(inp, ispart1):
    inp = [(l.split(' ')[0], int(l.split(' ')[1])) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
