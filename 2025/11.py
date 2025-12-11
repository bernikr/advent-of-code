import operator
from collections.abc import Iterable
from functools import reduce
from itertools import pairwise

import networkx as nx

from aocd_runner import aocd_run_solver


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp: dict[str, list[str]] = {k: v.split() for k, v in (line.split(":") for line in inp.splitlines())}
    g: nx.DiGraph[str] = nx.DiGraph()
    for k, v in inp.items():
        for vv in v:
            g.add_edge(k, vv)
    if "you" in g:
        yield 1, count_paths(g, "you", "out")
    if "svr" in g:
        assert nx.is_directed_acyclic_graph(g), "graph is not acyclic"
        if nx.has_path(g, "fft", "dac"):
            order = ["svr", "fft", "dac", "out"]
        else:
            assert nx.has_path(g, "dac", "fft"), "no connection between dac and fft"
            order = ["svr", "dac", "fft", "out"]
        yield 2, reduce(operator.mul, (count_paths(g, a, b) for a, b in pairwise(order)), 1)


# This needs to be optimized for part 2
def count_paths[T](g: "nx.DiGraph[T]", start: T, end: T) -> int:
    return len(list(nx.all_simple_paths(g, start, end)))


if __name__ == "__main__":
    aocd_run_solver(solve)
