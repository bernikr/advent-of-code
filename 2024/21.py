import itertools
from collections.abc import Iterable
from functools import cache

import networkx as nx
from tqdm import tqdm

from aoc_utils import DOWN, LEFT, RIGHT, UP, Vec, create_map


def parse_pad(pad: str) -> nx.DiGraph[str]:
    dirs = {"^": UP, "v": DOWN, "<": LEFT, ">": RIGHT}
    pad: dict[Vec, str] = {p: c for p, c in create_map(pad).items() if c != " "}
    g = nx.DiGraph[str]()
    for p, c in pad.items():
        for dc, d in dirs.items():
            if (np := p + d) in pad:
                g.add_edge(c, pad[np], dir=dc)
    return g


numpad = parse_pad("789\n456\n123\n 0A")
dirpad = parse_pad(" ^A\n<v>")


@cache
def seq_len(seq: str, level: int, pos: str = "A", *, first: bool = True) -> int:
    if not seq:
        return 0
    pad = numpad if first else dirpad
    path_lengths = []
    for path in nx.all_shortest_paths(pad, pos, seq[0]):
        new_seq = "".join(pad.edges[a, b]["dir"] for a, b in itertools.pairwise(path)) + "A"
        if level == 0:
            path_lengths.append(len(new_seq))
        else:
            path_lengths.append(seq_len(new_seq, level - 1, "A", first=False))
    return min(path_lengths) + seq_len(seq[1:], level, seq[0], first=first)


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = inp.splitlines()
    yield 1, sum(int(x[:-1]) * seq_len(x, 2) for x in tqdm(inp))
    yield 2, sum(int(x[:-1]) * seq_len(x, 25) for x in tqdm(inp))


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
