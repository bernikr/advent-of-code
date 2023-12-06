import math
import operator
import re
from functools import reduce


def solve(inp, part1):
    if not part1:
        inp = inp.replace(" ", "")
    times, distances = map(lambda l: [int(x) for x in re.findall(r"\d+", l)], inp.splitlines())
    return reduce(operator.mul, (math.ceil(-t / 2 + math.sqrt(t * t / 4 - d)) -
                                 math.floor(-t / 2 - math.sqrt(t * t / 4 - d)) - 1 for t, d in zip(times, distances)))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
