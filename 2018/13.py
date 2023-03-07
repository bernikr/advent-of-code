from dataclasses import dataclass
from itertools import count

from aoc_utils import Vec

dirs = "^>v<"
dir_map = {"^": Vec(0, -1), "v": Vec(0, 1), "<": Vec(-1, 0), ">": Vec(1, 0)}
turns = {r"\>": "v", "/>": "^", r"\^": "<", "/<": "v", r"\<": "^", r"\v": ">", "/v": "<", "/^": ">"}


def intersection(dir, state):
    i = dirs.index(dir) + state
    if i >= 4: i -= 4
    if i < 0: i += 4
    state += 1
    if state > 1: state -= 3
    return dirs[i], state


@dataclass
class Cart:
    pos: Vec
    dir: chr
    state: int = -1


def solve(inp, part1):
    carts = []
    mapp = {}
    for y, l in enumerate(inp.splitlines()):
        for x, c in enumerate(l):
            pos = Vec(x, y)
            if c in "<>v^":
                carts.append(Cart(pos, c))
                c = {"<": "-", ">": "-", "^": "|", "v": "|"}[c]
            if c in r"|-\/+":
                mapp[pos] = c
    for _ in count():
        for c in sorted(carts, key=lambda x: (x.pos[1], x.pos[0])):
            c.pos += dir_map[c.dir]
            if any(c.pos == c2.pos for c2 in carts if c != c2):
                if part1:
                    return "{},{}".format(*c.pos)
                else:
                    carts = [c2 for c2 in carts if c2.pos != c.pos]
            p = mapp[c.pos]
            if p in "|-":
                pass
            elif p in r"\/":
                c.dir = turns[p + c.dir]
            elif p == "+":
                c.dir, c.state = intersection(c.dir, c.state)
        if not part1 and len(carts) == 1:
            return "{},{}".format(*carts[0].pos)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
