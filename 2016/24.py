from functools import cache
from itertools import count

from aoc_utils import Vec, dirs4


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


def solve(inp, ispart1):
    global mapp
    mapp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    return part1() if ispart1 else part2()


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
