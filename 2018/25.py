from itertools import product

from aoc_utils import Vec

neighborhood = [Vec(*d) for d in product(range(-3, 4), repeat=4) if Vec(*d).manhatten() <= 3]


def solve(inp, _):
    points = {Vec(*map(int, l.split(","))) for l in inp.splitlines()}
    consts = 0
    while points:
        q = [points.pop()]
        consts += 1
        while q:
            p = q.pop()
            visited = {p + d for d in neighborhood}
            found = points & visited
            points = points - found
            q.extend(found)
    return consts


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")  # noqa: FBT003
    except AocdError as e:
        print(e)
