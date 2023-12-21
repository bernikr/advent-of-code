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
        xmax, ymax = map(max, zip(*mapp))
        assert xmax == ymax  # assert quadratic input
        n = xmax + 1
        steps = 26501365
        a, r = steps // n, steps % n  # repeats and remainder

        seen = set()
        front = {start}
        count = [0, 0]
        counts = [0] * (n * 2 + r + 1)
        for i in range(n * 2 + r + 1):
            count[i % 2] += len(front)
            counts[i] = count[i % 2]
            seen |= front
            front = {(p + d) for p in front for d in dirs4 if (p + d).pos_mod(n) not in walls and p + d not in seen}

        poly = np.polyfit([0, 1, 2], [counts[a * n + r] for a in [0, 1, 2]], 2)
        x = (steps - r) // n
        return round(poly[0]) * x * x + round(poly[1]) * x + round(poly[2])


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
