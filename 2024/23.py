from collections.abc import Iterable

import networkx as nx


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    g = nx.Graph(l.split("-") for l in inp.splitlines())
    yield 1, sum(len(a) == 3 and any(x.startswith("t") for x in a) for a in nx.enumerate_all_cliques(g))
    yield 2, ",".join(sorted(max(nx.find_cliques(g), key=len)))  # type: ignore[arg-type]


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
