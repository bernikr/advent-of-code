from collections import defaultdict

from aoc_utils import Vec, Dir
from tqdm import tqdm

rules1 = {
    ".": ("#", lambda d: d.turn_left()),
    "#": (".", lambda d: d.turn_right()),
}

rules2 = {
    ".": ("W", lambda d: d.turn_left()),
    "W": ("#", lambda d: d),
    "#": ("F", lambda d: d.turn_right()),
    "F": (".", lambda d: d.turn_left().turn_left()),
}


def solve(inp, part1):
    inp = inp.splitlines()
    sizex, sizey = len(inp[0]), len(inp)
    mapp = defaultdict(lambda: ".", {Vec(x, y): c for y, l in enumerate(inp) for x, c in enumerate(l)})
    pos = Vec(sizex // 2, sizey // 2)
    dir = Dir.UP
    count = 0
    rules = rules1 if part1 else rules2
    for _ in tqdm(range(10000 if part1 else 10000000)):
        new_state, action = rules[mapp[pos]]
        mapp[pos] = new_state
        dir = action(dir)
        pos += dir.value
        if new_state == "#":
            count += 1
    return count


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
