from collections import deque

from aoc_utils import Vec, dirs4
from aocd import data, submit, AocdError


def height_from_letter(c):
    if c == "S":
        c = "a"
    elif c == "E":
        c = "z"
    return ord(c) - ord("a")


def solve(inp, part1):
    inp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    start = next(pos for pos, c in inp.items() if c == "S")
    target = next(pos for pos, c in inp.items() if c == "E")
    inp = {pos: height_from_letter(c) for pos, c in inp.items()}

    dist = {target: 0}
    q = deque([target])
    while q:
        u = q.popleft()
        if (u == start) if part1 else (inp[u] == 0):
            return dist[u]

        for dir in dirs4:
            v = u + dir
            if v in inp and inp[v] >= inp[u] - 1:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q.append(v)


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
