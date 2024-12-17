from collections.abc import Iterable

from tqdm import tqdm

from aoc_utils import UP, Vec, create_map


def check_loop(mapp: dict[Vec, str]) -> bool:
    pos = next(p for p, c in mapp.items() if c == "^")
    d = UP
    visited = set()
    while (pos, d) not in visited and pos in mapp:
        visited.add((pos, d))
        if mapp.get(pos + d) != "#":
            pos += d
        else:
            d = d.turn_right()
    return (pos, d) in visited


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = create_map(inp)
    start = next(p for p, c in mapp.items() if c == "^")
    pos = start
    d = UP
    visited = set()
    while pos in mapp:
        visited.add(pos)
        if mapp.get(pos + d) != "#":
            pos += d
        else:
            d = d.turn_right()
    yield 1, len(visited)
    yield 2, sum(check_loop(mapp | {p: "#"}) for p in tqdm(visited) if p != start)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
