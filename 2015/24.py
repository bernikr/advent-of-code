import itertools
import operator
from functools import reduce


def solve(inp, part1):
    inp = list(map(int, inp.splitlines()))
    group_size = sum(inp) // (3 if part1 else 4)
    return next(reduce(operator.mul, x)
                for x in itertools.chain.from_iterable(itertools.combinations(inp, i)
                                                       for i in range(len(inp))) if sum(x) == group_size)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
