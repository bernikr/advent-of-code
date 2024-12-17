from collections.abc import Iterable

from aoc_utils import DOWN, LEFT, RIGHT, UP, Vec, create_map

dir_mapping = {"^": UP, "v": DOWN, ">": RIGHT, "<": LEFT}


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp, directions = inp.split("\n\n")
    directions = [dir_mapping[d] for d in directions.replace("\n", "")]
    yield 1, solve_part(directions, mapp)
    yield 2, solve_part(directions, mapp, part2=True)


def push_boxes(pos: Vec, d: Vec, boxes: set[Vec], mapp: dict[Vec, str], *, part2: bool) -> tuple[bool, dict[Vec, Vec]]:
    if mapp[pos + d] == "#":
        return False, {}

    box_updates = {}
    success = True

    possible_box_pos = ({pos + d, pos + d + LEFT} if part2 else {pos + d}) & boxes
    if possible_box_pos:
        box_pos = possible_box_pos.pop()
        box_updates[box_pos] = box_pos + d

        s, u = push_boxes(box_pos, d, boxes - {box_pos}, mapp, part2=part2)
        success &= s
        box_updates.update(u)

        if part2:
            s, u = push_boxes(box_pos + RIGHT, d, boxes - {box_pos}, mapp, part2=part2)
            success &= s
            box_updates.update(u)
    if success:
        return True, box_updates
    return False, {}


def solve_part(directions: list[Vec], mapp: str, *, part2: bool = False) -> int:
    if part2:
        for a, b in {"#": "##", "O": "[]", ".": "..", "@": "@."}.items():
            mapp = mapp.replace(a, b)
    mapp = create_map(mapp)
    robot = next(p for p, c in mapp.items() if c == "@")
    boxes = {p for p, c in mapp.items() if c in {"[", "O"}}
    for d in directions:
        success, box_updates = push_boxes(robot, d, boxes, mapp, part2=part2)
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
