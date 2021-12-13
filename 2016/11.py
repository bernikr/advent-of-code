import re
from itertools import chain, combinations, count

from aocd import get_data
from frozendict import frozendict


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


def regress(move, old_state):
    old_low_lv = next(i for i in range(1, 5) if old_state[1][i])
    new_low_lv = next(i for i in range(1, 5) if move[1][i])
    return old_low_lv > new_low_lv


def prune(moves, old_state):
    for move in moves:
        if not regress(move, old_state):
            yield move


def part1(inp):
    boundary = {(1, frozendict(inp))}
    visited = boundary.copy()
    for i in count(1):
        nb = set()
        for b in boundary:
            for move in prune(possible_moves(b), b):
                if is_done(move):
                    return i
                if move not in visited:
                    nb.add(move)
                    visited.add(move)
        boundary = nb


def part2(inp):
    return None


if __name__ == '__main__':
    data = get_data(day=11, year=2016)
    inp = {{'first': 1, 'second': 2, 'third': 3, 'fourth': 4}[f]:
               frozenset({e[:2] if e.endswith('microchip') else e[:2].upper()
                          for e in re.findall(r'\w+ generator|\w+-compatible microchip', c)})
           for f, c in (re.match(r'^The (.+) floor contains (.+)\.$', l).groups() for l in data.splitlines())}
    print(part1(inp))
    # print(part2(inp))
