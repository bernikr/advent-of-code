import re

import numpy as np
from aocd import data, submit, AocdError
from cpmpy import *

exp = re.compile(r"^Valve ([A-Z]{2}) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? ([A-Z, ]+)$", re.MULTILINE)


def solve(inp, part1):
    inp = [(a, int(b), c.split(', ')) for a, b, c in exp.findall(inp)]
    size = len(inp)
    name_to_index = {name: i for i, (name, _, _) in enumerate(sorted(inp))}
    valve_rates = np.zeros(size, dtype=int)
    connections = np.zeros((size, size), dtype=int)
    for name, rate, conns in inp:
        i = name_to_index[name]
        valve_rates[i] = rate
        connections[i, i] = 1
        for c in conns:
            connections[i, name_to_index[c]] = 1

    time = 30 if part1 else 26

    m = Model()
    pos = intvar(0, 1, shape=(time, size), name="p")
    pos2 = intvar(0, 1, shape=(time, size), name="p2")
    open_valves = intvar(0, 1, shape=(time, size), name="v")

    if part1:
        m += pos2 == 0

    # Start in AA
    for i in range(size):
        m += pos[0, i] == (i == name_to_index['AA'])
        if not part1:
            m += pos2[0, i] == (i == name_to_index['AA'])

    # Only move through available connections
    for i in range(1, time):
        m += sum(pos[i,]) == 1
        m += (pos[i,]).dot(connections).dot(pos[i - 1]) == 1
        if not part1:
            m += sum(pos2[i,]) == 1
            m += (pos2[i,]).dot(connections).dot(pos2[i - 1]) == 1

    # Start with all valves closed
    m += sum(open_valves[0,]) == 0

    # Only allow a valve to change when pos is there:
    for i in range(1, time):
        for v in range(size):
            m += (open_valves[i - 1, v] != open_valves[i, v]).implies(pos[i - 1, v] + pos2[i - 1, v] >= 1)
            m += (open_valves[i - 1, v] != open_valves[i, v]).implies(pos[i, v] + pos2[i, v] >= 1)

    m.maximize(sum(open_valves.dot(valve_rates)))
    if m.solve():
        return m.objective_value()


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
