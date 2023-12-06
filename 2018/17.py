import re
from itertools import chain

from aoc_utils import Vec, DOWN, RIGHT, LEFT, UP


def solve(inp, part1):
    inp = [re.search(r'(x|y)=(\d+), (x|y)=(\d+)\.\.(\d+)', l).groups() for l in inp.splitlines()]
    inp = list(chain.from_iterable(((dim, int(s), x) for x in range(int(a), int(b) + 1)) for dim, s, _, a, b in inp))
    clay = {Vec(a, b) if dim == 'x' else Vec(b, a) for dim, a, b in inp}
    maxy = max(y for _, y in clay)
    miny = min(y for _, y in clay)
    active_water = {Vec(500, 0)}
    all_water = set()
    standing_water = set()
    while active_water:
        cur = active_water.pop()
        all_water.add(cur)
        d = cur + DOWN
        if d not in clay and d not in all_water and d[1] <= maxy:
            active_water.add(d)
        if d in clay or d in standing_water:
            row = {cur}
            closed = True

            p = cur
            while True:
                p += RIGHT
                if p in clay:
                    break
                row.add(p)
                if p + DOWN not in clay and p + DOWN not in standing_water:
                    closed = False
                    active_water.add(p + DOWN)
                    break
            p = cur
            while True:
                p += LEFT
                if p in clay:
                    break
                row.add(p)
                if p + DOWN not in clay and p + DOWN not in standing_water:
                    closed = False
                    active_water.add(p + DOWN)
                    break
            all_water |= row
            if closed:
                standing_water |= row
                active_water.add(cur + UP)
    if part1:
        return len({c for c in all_water if miny <= c[1] <= maxy})
    else:
        return len(standing_water)


if __name__ == '__main__':
    from aocd import AocdError, submit, data

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
