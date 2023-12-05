import operator
import re
from functools import reduce

import portion as P
from more_itertools import batched


class IntInterval(P.AbstractDiscreteInterval):
    _step = 1


P = P.create_api(IntInterval)


def map_intervals(x, mappings):
    remaining = x
    new = P.empty()
    for dest_start, source_start, length in mappings:
        source_int = P.closed(source_start, source_start + length - 1)
        remaining -= source_int
        overlap = x & source_int
        shift = dest_start - source_start
        new |= overlap.apply(lambda i: i.replace(lower=lambda v: v + shift, upper=lambda v: v + shift))
    return remaining | new


def solve(inp, part1):
    seeds, *inp = inp.split("\n\n")
    seeds = list(map(int, re.findall(r"\d+", seeds)))
    mapss = [[tuple(map(int, res)) for res in re.findall(r"(\d+) (\d+) (\d+)", m)] for m in inp]
    if part1:
        x = reduce(operator.or_, (P.singleton(x) for x in seeds))
    else:
        x = reduce(operator.or_, (P.closed(a, a + b - 1) for a, b in batched(seeds, 2)))
    for maps in mapss:
        x = map_intervals(x, maps)
    return x.lower


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
