from itertools import product

from aoc_utils import Vec
from aocd import data, submit, AocdError
from tqdm import tqdm

dirs = [Vec(1, 0, 0), Vec(-1, 0, 0), Vec(0, 1, 0), Vec(0, -1, 0), Vec(0, 0, 1), Vec(0, 0, -1)]


def fill_void(start, mapp):
    maxv = max(map(max, mapp))
    stack = [start]
    visited = set()
    while stack:
        pos = stack.pop()
        visited.add(pos)
        if min(pos) < 0 or max(pos) > maxv:
            return []
        for d in dirs:
            n = pos + d
            if n not in visited and n not in mapp:
                stack.append(n)
    return visited


def solve(inp, part1):
    inp = [Vec(*map(int, l.split(','))) for l in inp.splitlines()]
    if not part1:
        for pos in tqdm(product(range(max(map(max, inp)) + 1), repeat=3)):
            pos = Vec(*pos)
            if pos not in inp:
                inp.extend(fill_void(pos, inp))
    return sum(sum(1 for d in dirs if c + d not in inp) for c in inp)


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
