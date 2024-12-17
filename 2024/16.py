from collections.abc import Iterable

import networkx as nx

from aoc_utils import RIGHT, create_map, dirs4


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = create_map(inp)
    start = next(p for p, c in mapp.items() if c == "S"), RIGHT
    ends = [(next(p for p, c in mapp.items() if c == "E"), d) for d in dirs4]
    g = nx.DiGraph()
    for p, c in mapp.items():
        if c != "#":
            g.add_weighted_edges_from(((p, d), (p + d, d), 1) for d in dirs4 if mapp.get(p + d, "#") != "#")
            g.add_weighted_edges_from(((p, d), (p, d.turn_left()), 1000) for d in dirs4)
            g.add_weighted_edges_from(((p, d), (p, d.turn_right()), 1000) for d in dirs4)
    end = object()
    g.add_weighted_edges_from((e, end, 0) for e in ends)
    yield 1, nx.shortest_path_length(g, start, end, weight="weight")
    paths = nx.all_shortest_paths(g, start, end, weight="weight")
    yield 2, len({p for path in paths for p, _ in path[:-1]})


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
