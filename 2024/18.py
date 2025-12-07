from collections.abc import Iterable
from itertools import product
from typing import Any

import networkx as nx

from aoc_utils import Vec, dirs4
from aocd_runner import NO_EXTRA, aocd_run_solver


def solve(inp: str, extra: dict[str, Any] = NO_EXTRA) -> Iterable[tuple[int, int | str]]:
    width = extra.get("width", 71)
    n_bytes = extra.get("n_bytes", 1024)

    inp = [Vec(*map(int, l.split(","))) for l in inp.splitlines()]
    mapp = set(map(Vec, product(range(width), repeat=2)))
    start, end = Vec(0, 0), Vec(width - 1, width - 1)
    g: nx.Graph[Vec] = nx.Graph()
    g.add_edges_from((p, p + d) for p in mapp for d in dirs4 if p + d in mapp)
    yield 1, int(nx.shortest_path_length(g.subgraph(mapp - set(inp[:n_bytes])), start, end))
    l, r = n_bytes, len(inp)
    while l < r:
        m = (l + r) // 2
        if nx.has_path(g.subgraph(mapp - set(inp[:m])), start, end):
            l = m + 1
        else:
            r = m
    yield 2, f"{inp[l - 1].x},{inp[l - 1].y}"


if __name__ == "__main__":
    aocd_run_solver(solve)
