from operator import itemgetter

from aoc_utils import Vec, dirs4, UP, RIGHT, DOWN, LEFT

dir_change = {
    ".": {d: [d] for d in dirs4},
    "/": {UP: [RIGHT], RIGHT: [UP], DOWN: [LEFT], LEFT: [DOWN]},
    "\\": {UP: [LEFT], LEFT: [UP], DOWN: [RIGHT], RIGHT: [DOWN]},
    "-": {UP: [LEFT, RIGHT], DOWN: [LEFT, RIGHT], LEFT: [LEFT], RIGHT: [RIGHT]},
    "|": {UP: [UP], DOWN: [DOWN], LEFT: [UP, DOWN], RIGHT: [UP, DOWN]},
}


def energize(mapp, start):
    active = [start]
    visited = set()
    while active:
        pos, dir = active.pop()
        pos += dir
        if pos in mapp and (pos, dir) not in visited:
            visited.add((pos, dir))
            ds = dir_change[mapp[pos]][dir]
            active += [(pos, d) for d in ds]
    return len(set(map(itemgetter(0), visited)))


def solve(inp, part1):
    mapp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    if part1:
        return energize(mapp, (Vec(-1, 0), RIGHT))
    else:
        xmax, ymax = map(max, zip(*mapp.keys()))
        starts = [(Vec(-1, y), RIGHT) for y in range(ymax + 1)] + \
                 [(Vec(xmax + 1, y), LEFT) for y in range(ymax + 1)] + \
                 [(Vec(x, -1), DOWN) for x in range(xmax + 1)] + \
                 [(Vec(x, ymax + 1), UP) for x in range(xmax + 1)]
        return max(energize(mapp, s) for s in starts)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
