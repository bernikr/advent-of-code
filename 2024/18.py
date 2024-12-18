from collections.abc import Iterable
from itertools import product

import networkx as nx

from aoc_utils import Vec, dirs4


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = [Vec(*map(int, l.split(","))) for l in inp.splitlines()]
    mapp = set(map(Vec, product(range(71), repeat=2))) - set(inp[:1024])
    start, end = Vec(0, 0), Vec(70, 70)
    g = nx.Graph()
    for p in mapp:
        g.add_node(p)
        g.add_edges_from((p, p + d) for d in dirs4 if p + d in mapp)
    yield 1, nx.shortest_path_length(g, start, end)
    for p in inp[1024:]:
        g.remove_node(p)
        if not nx.has_path(g, start, end):
            yield 2, f"{p.x},{p.y}"
            return


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
