from itertools import count

from aoc_utils import Vec, dirs4


def is_non_negative(c):
    return all(a >= 0 for a in c)


def is_wall(c, fav):
    x, y = c
    return sum(int(i) for i in format(x * x + 3 * x + 2 * x * y + y + y * y + fav, 'b')) % 2 != 0


def part1(inp):
    boundary = {Vec(1, 1)}
    visited = boundary.copy()
    for i in count(1):
        nb = set()
        for b in boundary:
            for d in dirs4:
                nc = b + d
                if nc == (31, 39):
                    return i
                if nc not in visited and is_non_negative(nc) and not is_wall(nc, inp):
                    nb.add(nc)
                    visited.add(nc)
        boundary = nb


def part2(inp):
    boundary = {Vec(1, 1)}
    visited = boundary.copy()
    for _ in range(50):
        nb = set()
        for b in boundary:
            for d in dirs4:
                nc = b + d
                if nc not in visited and is_non_negative(nc) and not is_wall(nc, inp):
                    nb.add(nc)
                    visited.add(nc)
        boundary = nb
    return len(visited)


def solve(inp, ispart1):
    inp = int(inp)
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
