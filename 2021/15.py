from itertools import product

from aoc_utils import Vec, dirs4, a_star


def solve(inp, part1):
    mapp = {Vec(x, y): int(v) for y, l in enumerate(inp.splitlines()) for x, v in enumerate(l)}
    if not part1:
        nmap = {}
        lx, ly = max(x for x, _ in mapp) + 1, max(y for _, y in mapp) + 1
        for (x, y), v in mapp.items():
            for a, b in product(range(5), repeat=2):
                nv = (v + a + b) % 9
                nmap[Vec(x + a * lx, y + b * ly)] = 9 if nv == 0 else nv
        mapp = nmap

    start = Vec(0, 0)
    goal = max(mapp, key=sum)
    neighbors = lambda s: (s + dir for dir in dirs4 if (s + dir) in mapp)
    d = lambda c, n: mapp[n]
    h = lambda s: (s - goal).manhatten()
    return a_star(start, goal, neighbors, h, d)[1]


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
