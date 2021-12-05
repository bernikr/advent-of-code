import operator
from enum import Enum
from functools import cache

from aocd import get_data


class Dir(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def move(self, c):
        return tuple(map(operator.add, c, self.value))


@cache
def find(letter):
    cs = [c for c, v in mapp.items() if v == letter]
    assert len(cs) == 1
    return cs[0]


@cache
def steps_to_available_keys(start_pos, current_keys):
    boundary = {find(start_pos)}
    visited = boundary.copy()
    res = {}
    steps = 1
    while boundary:
        nb = set()
        for b in boundary:
            for d in Dir:
                nc = d.move(b)
                if nc in visited:
                    continue
                match mapp[nc]:
                    case "." | "@":
                        nb.add(nc)
                        visited.add(nc)
                    case x if x.lower() in current_keys:
                        nb.add(nc)
                        visited.add(nc)
                    case k if k.islower() and k not in current_keys:
                        res[k] = steps
        boundary = nb
        steps += 1
    return res


@cache
def min_steps(pos, keys):
    key_distances = steps_to_available_keys(pos, keys)
    if not key_distances:
        return 0
    return min(d + min_steps(k, keys.union({k})) for k, d in key_distances.items())


def part1():
    return min_steps('@', frozenset())


def part2():
    return None


if __name__ == '__main__':
    data = get_data(day=18, year=2019)
    mapp: dict[tuple[int, int], str] = {(x, y): c for y, l in enumerate(data.splitlines()) for x, c in enumerate(l)}
    print(part1())
    print(part2())
