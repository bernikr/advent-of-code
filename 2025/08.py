import operator
from collections.abc import Iterable
from functools import reduce
from heapq import heapify, heappop
from itertools import combinations, count
from typing import Any

import networkx as nx

from aoc_utils import Vec
from aocd_runner import NO_EXTRA, aocd_run_solver


def solve(inp: str, extra: dict[str, Any] = NO_EXTRA) -> Iterable[tuple[int, int | str]]:
    boxes: set[Vec] = {Vec(*map(int, line.split(","))) for line in inp.splitlines()}
    distances: list[tuple[int, Vec, Vec]] = [((b - a).distance_squared(), a, b) for a, b in combinations(boxes, 2)]
    heapify(distances)
    g: nx.Graph[Vec] = nx.Graph()
    g.add_nodes_from(boxes)
    for i in count(1):
        _, a, b = heappop(distances)
        g.add_edge(a, b)
        if i == extra.get("n_pairs", 1000):
            yield 1, reduce(operator.mul, sorted(map(len, nx.connected_components(g)), reverse=True)[:3])
        if nx.is_connected(g):
            yield 2, a.x * b.x
            return


if __name__ == "__main__":
    aocd_run_solver(solve)
