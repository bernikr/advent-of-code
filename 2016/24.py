from functools import cache
from itertools import count

from aoc_utils import Vec, dirs4
from aocd import get_data


@cache
def find(n):
    return next(p for p, c in mapp.items() if c == n)


@cache
def distances_from_point(startpos):
    boundary = {startpos}
    visited = boundary.copy()
    res = {}
    for i in count(1):
        nb = set()
        for b in boundary:
            for d in dirs4:
                if (b + d) not in visited and mapp.get(b + d, '#') != '#':
                    nb.add(b + d)
                    visited.add(b + d)
                    if mapp[b + d] != '.':
                        res[mapp[b + d]] = i
        boundary = nb
        if not boundary:
            return res


@cache
def shortest_distance(pos, collected):
    try:
        return min(d + shortest_distance(p, collected.union({p}))
                   for p, d in distances_from_point(find(pos)).items() if p not in collected and p != '0')
    except ValueError:
        return 0


def part1():
    return shortest_distance('0', frozenset())


@cache
def shortest_distance_return(pos, collected):
    try:
        return min(d + shortest_distance_return(p, collected.union({p}))
                   for p, d in distances_from_point(find(pos)).items() if p not in collected and p != '0')
    except ValueError:
        return distances_from_point(find(pos))['0']


def part2():
    return shortest_distance_return('0', frozenset())


if __name__ == '__main__':
    data = get_data(day=24, year=2016)
    mapp = {Vec(x, y): c for y, l in enumerate(data.splitlines()) for x, c in enumerate(l)}
    print(part1())
    print(part2())
