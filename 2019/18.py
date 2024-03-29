import operator
from collections import defaultdict
from enum import Enum
from functools import cache
from itertools import chain

from frozendict import frozendict


class Dir(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def move(self, c):
        return tuple(map(operator.add, c, self.value))


def find(mapp, letter):
    cs = [c for c, v in mapp.items() if v == letter]
    assert len(cs) == 1
    return cs[0]


@cache
def steps_and_requirements_to_keys(mapp, start_pos):
    boundary = {(find(mapp, start_pos), frozenset())}
    visited = defaultdict(lambda: [], {find(mapp, start_pos): [frozenset()]})
    res = defaultdict(lambda: [])
    steps = 1
    while boundary:
        nb = set()
        for b, keys in boundary:
            for d in Dir:
                nc = d.move(b)
                if nc in visited and any(reqs.issubset(keys) for reqs in visited[nc]):
                    continue
                match mapp[nc]:
                    case "." | "@" | "1" | "2" | "3" | "4":
                        nb.add((nc, keys))
                        visited[nc].append(keys)
                    case k if k.islower():
                        nb.add((nc, keys))
                        visited[nc].append(keys)
                        res[k].append((keys, steps))
                    case door if door.isupper():
                        nb.add((nc, keys.union({door.lower()})))
                        visited[nc].append(keys.union({door.lower()}))
        boundary = nb
        steps += 1
    return res


@cache
def steps_to_available_keys(mapp, start_pos, current_keys):
    return {k: min(d for reqs, d in req_dists if reqs.issubset(current_keys))
            for k, req_dists in steps_and_requirements_to_keys(mapp, start_pos).items()
            if any(reqs.issubset(current_keys) for reqs, d in req_dists) and k not in current_keys}


@cache
def min_steps(mapp, pos, keys):
    key_distances = steps_to_available_keys(mapp, pos, keys)
    if not key_distances:
        return 0
    return min(d + min_steps(mapp, k, keys.union({k})) for k, d in key_distances.items())


def part1(inp):
    return min_steps(frozendict(inp), '@', frozenset())


@cache
def min_steps_multi(mapp, poss, keys):
    key_distances = list(chain.from_iterable(
        ((start, k, d) for k, d in steps_to_available_keys(mapp, start, keys).items()) for start in poss))
    if not key_distances:
        return 0
    return min(d + min_steps_multi(mapp, poss.difference({start}).union({k}), keys.union({k})) for start, k, d in
               key_distances)


def part2(inp):
    new_mapp = inp.copy()
    new_middle = {
        (0, 0): '#', (0, 1): '#', (0, -1): '#', (1, 0): '#', (-1, 0): '#',
        (-1, -1): '1', (1, -1): '2', (-1, 1): '3', (1, 1): '4'
    }
    mx, my = find(new_mapp, '@')
    for (x, y), c in new_middle.items():
        new_mapp[(mx + x, my + y)] = c

    return min_steps_multi(frozendict(new_mapp), frozenset('1234'), frozenset())


def solve(inp, ispart1):
    inp = {(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
