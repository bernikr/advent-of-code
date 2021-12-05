import operator
from collections import defaultdict
from enum import Enum
from functools import cache

from aocd import get_data
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
                    case "." | "@":
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



def part2():
    return None


if __name__ == '__main__':
    data = get_data(day=18, year=2019)
    inp = {(x, y): c for y, l in enumerate(data.splitlines()) for x, c in enumerate(l)}
    print(part1(inp))
    print(part2(inp))
