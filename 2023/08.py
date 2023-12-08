import math
import re
from functools import reduce
from itertools import cycle


def solve1(path, mapp):
    pos = "AAA"
    for i, step in enumerate(cycle(path)):
        if pos == "ZZZ":
            return i
        pos = mapp[pos][step == "R"]


def get_ghost_cycle(path, mapp, ghost):
    pos = ghost
    visited = {}
    exits = []
    for step_count, (index, direction) in enumerate(cycle(enumerate(path))):
        if (index, pos) in visited:
            return visited[index, pos], step_count - visited[index, pos], exits
        visited[index, pos] = step_count
        if pos.endswith("Z"):
            exits.append(step_count)
        pos = mapp[pos][direction == "R"]


def solve2(path, mapp):
    ghosts = [a for a in mapp.keys() if a.endswith("A")]
    cycles = [get_ghost_cycle(path, mapp, g) for g in ghosts]
    assert all(length in ends for start, length, ends in cycles)  # code only works for inputs in this form
    return reduce(math.lcm, (l for _, l, _ in cycles))


def solve(inp, part1):
    inp = inp.splitlines()
    path = inp[0]
    mapp = {a: (b, c) for a, b, c in (re.search(r"(\S{3}) = \((\S{3}), (\S{3})\)", l).groups()
                                      for l in inp[2:])}
    if part1:
        return solve1(path, mapp)
    else:
        return solve2(path, mapp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    print(solve("""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""", False))
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
