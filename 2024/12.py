from collections.abc import Iterable

from aoc_utils import Vec, create_map, dirs4


def region_side_count(region: set[Vec]) -> int:
    count = 0
    for p in region:
        for d in dirs4:
            if p + d in region:
                continue
            if p + d.turn_right() in region and p + d + d.turn_right() not in region:
                continue
            count += 1
    return count


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = create_map(inp)
    todo = set(mapp.keys())
    price, price2 = 0, 0
    while todo:
        region_todo = {todo.pop()}
        region = region_todo.copy()
        fence = 0
        while region_todo:
            cur = region_todo.pop()
            for d in dirs4:
                if mapp.get(cur + d, "") == mapp[cur]:
                    if cur + d not in region:
                        region.add(cur + d)
                        region_todo.add(cur + d)
                else:
                    fence += 1
        todo -= region
        price += fence * len(region)
        price2 += len(region) * region_side_count(region)
    yield 1, price
    yield 2, price2


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
