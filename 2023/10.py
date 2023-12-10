from itertools import pairwise

from aoc_utils import Vec, dirs4

connections = {
    "-": (Vec(-1, 0), Vec(1, 0)),
    "|": (Vec(0, -1), Vec(0, 1)),
    "L": (Vec(0, -1), Vec(1, 0)),
    "J": (Vec(0, -1), Vec(-1, 0)),
    "7": (Vec(0, 1), Vec(-1, 0)),
    "F": (Vec(0, 1), Vec(1, 0)),
    ".": (),
}


def step(pr, ne, mapp):
    conn = connections[mapp[ne]]
    if pr - ne not in conn:
        return None
    return next(ne + c for c in conn if c != pr - ne)


def solve(inp, part1):
    mapp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    start = next(pos for pos, c in mapp.items() if c == "S")
    first = next(start + dir for dir in dirs4 if step(start, start + dir, mapp))
    loop = [start, first]
    while loop[0] != loop[-1]:
        loop.append(step(loop[-2], loop[-1], mapp))
    if part1:
        return len(loop) // 2
    else:
        # calculate polygon area by Shoelace formula https://en.wikipedia.org/wiki/Shoelace_formula
        area = abs(sum(a[0] * b[1] - a[1] * b[0] for a, b in pairwise(loop))) / 2
        # use Pick's Theorem to calculate the number of interior points https://en.wikipedia.org/wiki/Pick%27s_theorem
        return int(area - (len(loop) - 1) / 2 + 1)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
