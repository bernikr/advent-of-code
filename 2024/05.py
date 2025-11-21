from collections.abc import Iterable, Sequence

import networkx as nx


def is_valid(rules: Sequence[Sequence[int]], pages: Sequence[int]) -> bool:
    for rule in rules:
        if rule[0] in pages and rule[1] in pages and pages.index(rule[0]) > pages.index(rule[1]):
            return False
    return True


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    rules, pages = (
        [tuple(map(int, l.replace("|", ",").split(","))) for l in s.splitlines()] for s in inp.split("\n\n")
    )
    yield 1, sum(x[len(x) // 2] for x in pages if is_valid(rules, x))
    rules_graph = nx.DiGraph(rules)
    yield (
        2,
        sum(list(nx.topological_sort(rules_graph.subgraph(x)))[len(x) // 2] for x in pages if not is_valid(rules, x)),
    )


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
