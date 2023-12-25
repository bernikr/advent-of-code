import operator
import re
from functools import reduce

import networkx as nx


def solve(inp, part1):
    g = nx.Graph()
    for l in inp.splitlines():
        nx.add_star(g, re.findall(r"[a-z]{3}", l))
    res = nx.spectral_bisection(g)
    return reduce(operator.mul, map(len, res))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
    except AocdError as e:
        print(e)
