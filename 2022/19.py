import operator
import re
from functools import reduce

import numpy as np
from aocd import data, submit, AocdError
from cpmpy import *

resources = ["ore", "clay", "obsidian", "geode"]


def most_geodes(blueprint, t):
    costs = np.zeros(dtype=int, shape=(4, 4))

    for x, r in enumerate(resources):
        for y, c in enumerate(resources):
            costs[x, y] = blueprint[r].get(c, 0)

    m = Model()

    inventory = intvar(0, (t * t) // 2, shape=(t + 1, 4), name="inv")
    robots = intvar(0, t, shape=(t + 1, 4), name="r")
    factory = intvar(0, 1, shape=(t + 1, 4), name="f")

    m += inventory[0] == 0
    m += robots[0] == (1, 0, 0, 0)
    m += factory[0] == 0

    for i in range(t + 1):
        m += sum(factory[i]) <= 1

    for i in range(t):
        m += robots[i + 1] == robots[i] + factory[i]
        m += inventory[i] - factory[i + 1].dot(costs) >= 0
        m += inventory[i + 1] == inventory[i] + robots[i + 1] - factory[i + 1].dot(costs)

    m.maximize(inventory[-1, -1])
    m.solve()
    return m.objective_value()


def solve(inp, part1):
    exp1 = re.compile(r"([a-z]+) robot costs ([^.]+)")
    exp2 = re.compile(r"(\d+) ([a-z]+)")
    inp = [{a: {y: int(x) for x, y in exp2.findall(b)} for a, b in l}
           for l in (exp1.findall(l) for l in inp.splitlines())]
    if part1:
        return sum(i * most_geodes(blueprint, 24) for i, blueprint in enumerate(inp, 1))
    else:
        return reduce(operator.mul, (most_geodes(blueprint, 32) for blueprint in inp[:3]))


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
