import re
from itertools import chain, combinations

from frozendict import frozendict

from aoc_utils import a_star


def is_unsafe(floor):
    return not all(m.islower() for m in floor) and any(
        all(m.upper() != g for g in floor if g.isupper()) for m in floor if m.islower())


def possible_moves(state):
    lv, mapp = state
    next_stops = [l for l in [lv - 1, lv + 1] if 1 <= l <= 4]
    for items in chain(combinations(mapp[lv], 1), combinations(mapp[lv], 2)):
        for ns in next_stops:
            new_floor = mapp[ns].union(items)
            old_floor = mapp[lv].difference(items)
            if not is_unsafe(new_floor) and not is_unsafe(old_floor):
                yield ns, frozendict({f: new_floor if f == ns else old_floor if f == lv else content
                                      for f, content in mapp.items()})


def is_done(state):
    lv, mapp = state
    return lv == 4 and all(not mapp[i] for i in [1, 2, 3])


def simplify_state(state):
    elevator, stuff = state
    current_mapping = {}
    next_letter = 'A'
    res = {}
    for f, items in stuff.items():
        tmp = []
        for i in items:
            if i not in current_mapping:
                current_mapping[i.lower()] = next_letter.lower()
                current_mapping[i.upper()] = next_letter.upper()
                next_letter = chr(ord(next_letter) + 1)
            tmp.append(current_mapping[i])
        res[f] = frozenset(tmp)
    return elevator, frozendict(res)


def h(state):
    return 4 - state[0] + sum((4 - f) * len(v) for f, v in state[1].items())


def solve(inp, part1):
    inp = {{'first': 1, 'second': 2, 'third': 3, 'fourth': 4}[f]:
               frozenset({e[:2] if e.endswith('microchip') else e[:2].upper()
                          for e in re.findall(r'\w+ generator|\w+-compatible microchip', c)})
           for f, c in (re.match(r'^The (.+) floor contains (.+)\.$', l).groups() for l in inp.splitlines())}

    if not part1:
        inp[1] = inp[1].union({'EL', 'el', 'DI', 'di'})

    start = simplify_state((1, frozendict(inp)))
    neighbors = lambda s: (simplify_state(n) for n in possible_moves(s))
    return a_star(start, is_done, neighbors, lambda a, b: 1)[1]


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
