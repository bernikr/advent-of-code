import numpy as np

from aoc_utils import Vec, dirs4


def solve(inp, part1):
    mapp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    start = next(p for p, c in mapp.items() if c == "S")
    walls = {p for p, c in mapp.items() if c == "#"}
    if part1:
        seen = set()
        front = {start}
        count = 0
        for i in range(64 + 1):
            if i % 2 == 0:
                count += len(front)
            seen |= front
            front = {p + d for p in front for d in dirs4 if p + d not in walls and p + d not in seen}
        return count
    else:
        n, _ = Vec(1, 1) + map(max, zip(*mapp))
        steps = 26501365
        x, r = steps // n, steps % n  # repeats and remainder

        seen = set()
        front = {start}
        count = [0, 0]
        counts = [0] * (n * 2 + r + 1)
        for i in range(n * 2 + r + 1):
            count[i % 2] += len(front)
            counts[i] = count[i % 2]
            seen |= front
            front = {(p[0] + d[0], p[1] + d[1]) for p in front for d in dirs4
                     if (((p[0] + d[0]) % n + n) % n, ((p[1] + d[1]) % n + n) % n) not in walls
                     and (p[0] + d[0], p[1] + d[1]) not in seen}

        poly = tuple(map(round, np.polyfit([0, 1, 2], [counts[a * n + r] for a in [0, 1, 2]], 2)))
        return poly[0] * x * x + poly[1] * x + poly[2]


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
