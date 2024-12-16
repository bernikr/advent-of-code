from collections.abc import Iterable

from aoc_utils import LEFT, Vec, a_star, reconstruct_paths


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    start = next(p for p, c in mapp.items() if c == "S"), LEFT
    end = next(p for p, c in mapp.items() if c == "E")
    is_end = lambda s: s[0] == end

    def get_neighbors(s: tuple[Vec, Vec]) -> Iterable[tuple[tuple[Vec, Vec], int]]:
        p, d = s
        if mapp.get(p + d, "#") != "#":
            yield (p + d, d), 1
        yield (p, d.turn_left()), 1000
        yield (p, d.turn_right()), 1000

    predecessors, score = a_star(start, is_end, get_neighbors)
    yield 1, score

    paths = []
    for end_state in ((a, b) for a, b in predecessors if a == end):
        paths += list(reconstruct_paths(predecessors, end_state))
    yield 2, len({p for path in paths for p, _ in path})


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
