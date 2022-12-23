from collections import deque, defaultdict
from itertools import count

from aoc_utils import Vec, dirs8
from aocd import data, submit, AocdError
from tqdm import tqdm

N, S, E, W = Vec(0, -1), Vec(0, 1), Vec(1, 0), Vec(-1, 0)
NE, NW, SE, SW = N + E, N + W, S + E, S + W


def solve(inp, part1):
    elves = {Vec(x, y) for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l) if c == '#'}
    prev_elves = {}
    dirs = deque([N, S, W, E])
    look_dirs = {N: [N, NE, NW], S: [S, SE, SW], W: [W, NW, SW], E: [E, NE, SE]}
    for i in tqdm(count()):
        if part1 and i == 10:
            xmin, ymin = map(min, zip(*elves))
            xmax, ymax = map(max, zip(*elves))
            return (xmax - xmin + 1) * (ymax - ymin + 1) - len(elves)
        if not part1 and prev_elves == elves:
            return i
        proposed = []
        occupancy = defaultdict(lambda: 0)
        for e in elves:
            e_prop = e
            if any(e + d in elves for d in dirs8):
                for step_dir in list(dirs):
                    if all(e + d not in elves for d in look_dirs[step_dir]):
                        e_prop = e + step_dir
                        break
            proposed.append((e, e_prop))
            occupancy[e_prop] += 1
        dirs.rotate(-1)
        prev_elves = elves
        elves = {nextpos if occupancy[nextpos] == 1 else currentpos for currentpos, nextpos in proposed}


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
