from collections import Counter
from collections.abc import Iterable
from functools import cache
from itertools import product

import networkx as nx
from tqdm import tqdm

from aoc_utils import Vec, create_map, dirs4


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = create_map(inp)
    start = next(p for p, c in mapp.items() if c == "S")
    end = next(p for p, c in mapp.items() if c == "E")
    g = nx.Graph[Vec]()
    for p, c in mapp.items():
        if c != "#":
            g.add_edges_from((p, p + d) for d in dirs4 if mapp.get(p + d, "#") != "#")
    path = nx.shortest_path(g, start, end)
    yield 1, count_cheats(path, 2)
    yield 2, count_cheats(path, 20)


@cache
def dists(dist: int) -> list[Vec]:
    return list(filter(lambda p: p.manhatten() <= dist, (Vec(a) for a in product(range(-dist, dist + 1), repeat=2))))


def count_cheats(path: list[Vec], cheat_time: int) -> int:
    counts = Counter[float]()
    indecies = {p: i for i, p in enumerate(path)}
    for i, p in enumerate(tqdm(path)):
        for d in dists(cheat_time):
            if (a := indecies.get(p + d, -1) - i - d.manhatten()) > 0:
                counts[a] += 1
    return sum(c for x, c in counts.items() if x >= 100)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
