import math
import re
from dataclasses import dataclass

from aoc_utils import Vec, ocr10


@dataclass
class Point:
    pos: Vec
    vel: Vec


def solve(inp, part1):
    ex = re.compile(r"<\s*(-?\d+),\s*(-?\d+)\s*>")
    inp = [Point(*map(lambda c: Vec(int(c[0]), int(c[1])), ex.findall(l))) for l in inp.splitlines()]
    minspan = math.inf
    max_y_speed = max(map(lambda p: abs(p.vel[1]), inp))
    t = 0
    timestep = 0
    while True:
        yvals = list(map(lambda p: p.pos[1], inp))
        span = max(yvals) - min(yvals)
        last_timestep = timestep
        timestep = max(1, int(span / 2 / max_y_speed) - 5)
        t += timestep
        for p in inp:
            p.pos += p.vel * timestep
        if span < minspan:
            minspan = span
        else:
            t -= (timestep + last_timestep)
            for p in inp:
                p.pos -= p.vel * (timestep + last_timestep)
            xvals = list(map(lambda p: p.pos[0], inp))
            xmin, xmax = min(xvals), max(xvals)
            yvals = list(map(lambda p: p.pos[1], inp))
            ymin, ymax = min(yvals), max(yvals)
            ps = {p.pos - Vec(xmin, ymin) for p in inp}
            # print("\n".join("".join("#" if (x,y) in ps else "." for x in range(xmax-xmin+1)) for y in range(ymax-ymin+1)))
            if part1:
                return ocr10(ps)
            else:
                return t


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
