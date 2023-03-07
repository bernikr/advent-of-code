from collections import Counter
from itertools import count
from operator import itemgetter

from aoc_utils import Vec, dirs8
from frozendict import frozendict
from tqdm import tqdm


def apply_rule(state, pos):
    neighbors = [pos + d for d in dirs8 if pos + d in state]
    c = Counter(state[n] for n in neighbors)
    p = state[pos]
    if p == "." and c["|"] >= 3:
        return "|"
    if p == "|" and c["#"] >= 3:
        return "#"
    if p == "#" and (c["#"] == 0 or c["|"] == 0):
        return "."
    return p


def step(state):
    return {Vec(x, y): apply_rule(state, Vec(x, y))
            for x in range(max(map(itemgetter(0), state.keys())) + 1)
            for y in range(max(map(itemgetter(1), state.keys())) + 1)}


def solve(inp, part1):
    state = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    steps = 10
    if not part1:
        seen_states = {}
        for i in tqdm(count(1)):
            state = frozendict(step(state))
            if state in seen_states:
                steps = (1000000000 - i) % (i - seen_states[state])
                break
            seen_states[state] = i
    for _ in range(steps):
        state = step(state)
    return sum(1 for c in state.values() if c == "#") * sum(1 for c in state.values() if c == "|")


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
