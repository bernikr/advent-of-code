from collections.abc import Iterable

from aoc_utils import DOWN, LEFT, RIGHT, UP, Vec

dir_mapping = {"^": UP, "v": DOWN, ">": RIGHT, "<": LEFT}


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp, directions = inp.split("\n\n")
    directions = [dir_mapping[d] for d in directions.replace("\n", "")]
    yield 1, solve_part1(directions, mapp)
    yield 2, solve_part2(directions, mapp)


def solve_part1(directions: list[Vec], mapp: str) -> int:
    mapp = {Vec(x, y): c for y, l in enumerate(mapp.splitlines()) for x, c in enumerate(l)}
    robot = next(p for p, c in mapp.items() if c == "@")
    boxes = {p for p, c in mapp.items() if c == "O"}
    for d in directions:
        p = robot + d
        if mapp[p] == "#":
            continue
        if p not in boxes:
            robot = p
            continue
        while mapp[p] != "#" and p in boxes:
            p += d
        if mapp[p] != "#":
            robot += d
            boxes.remove(robot)
            boxes.add(p)
    return sum(y * 100 + x for x, y in boxes)


def push_boxes(pos: Vec, d: Vec, boxes: set[Vec], mapp: dict[Vec, str]) -> tuple[bool, dict[Vec, Vec]]:
    if mapp[pos + d] == "#":
        return False, {}

    box_updates = {}
    success = True

    possible_box_pos = {pos + d, pos + d + LEFT} & boxes
    if possible_box_pos:
        box_pos = possible_box_pos.pop()
        box_updates[box_pos] = box_pos + d

        s, u = push_boxes(box_pos, d, boxes - {box_pos}, mapp)
        success &= s
        box_updates.update(u)

        s, u = push_boxes(box_pos + RIGHT, d, boxes - {box_pos}, mapp)
        success &= s
        box_updates.update(u)
    if success:
        return True, box_updates
    return False, {}


def solve_part2(directions: list[Vec], mapp: str) -> int:
    for a, b in {"#": "##", "O": "[]", ".": "..", "@": "@."}.items():
        mapp = mapp.replace(a, b)
    mapp = {Vec(x, y): c for y, l in enumerate(mapp.splitlines()) for x, c in enumerate(l)}
    robot = next(p for p, c in mapp.items() if c == "@")
    boxes = {p for p, c in mapp.items() if c == "["}
    for d in directions:
        success, box_updates = push_boxes(robot, d, boxes, mapp)
        if success:
            boxes -= set(box_updates.keys())
            boxes |= set(box_updates.values())
            robot += d
    return sum(y * 100 + x for x, y in boxes)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
