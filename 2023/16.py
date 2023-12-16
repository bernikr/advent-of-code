from aoc_utils import Vec, dirs4, UP, RIGHT, DOWN, LEFT

dir_change = {
    ".": {d: d for d in dirs4},
    "/": {UP: RIGHT, RIGHT: UP, DOWN: LEFT, LEFT: DOWN},
    "\\": {UP: LEFT, LEFT: UP, DOWN: RIGHT, RIGHT: DOWN},
    "-": {UP: None, DOWN: None, LEFT: LEFT, RIGHT: RIGHT},
    "|": {UP: UP, DOWN: DOWN, LEFT: None, RIGHT: None},
}

split_dirs = {
    "-": [LEFT, RIGHT],
    "|": [UP, DOWN],
}


def energize_to_split(mapp, pos, dir):
    visited = set()
    while pos + dir in mapp:
        pos += dir
        visited.add(pos)
        dir = dir_change[mapp[pos]][dir]
        if dir is None:
            return visited, pos
    return visited, None


def energize(mapp, pos, dir):
    queue = [(pos, dir)]
    seen_splits = set()
    visited = set()
    while queue:
        pos, dir = queue.pop()
        nv, split = energize_to_split(mapp, pos, dir)
        visited |= nv
        if split is not None and split not in seen_splits:
            queue += [(split, d) for d in split_dirs[mapp[split]]]
            seen_splits.add(split)
    return visited


def build_fastmap(mapp):
    seen_by_split = {}
    for p, c in mapp.items():
        if c in "-|":
            seen1, goal1 = energize_to_split(mapp, p, split_dirs[c][0])
            seen2, goal2 = energize_to_split(mapp, p, split_dirs[c][1])
            seen_by_split[p] = ({p}, {goal1, goal2} - {None}, {p} | seen1 | seen2)
    for split, (resolved, unresolved, visited) in seen_by_split.items():
        while unresolved:
            u = unresolved.pop()
            resolved |= seen_by_split[u][0]
            unresolved |= seen_by_split[u][1]
            visited |= seen_by_split[u][2]
            unresolved -= resolved
        seen_by_split[split] = (resolved, unresolved, visited)
    return {a: b for a, (_, _, b) in seen_by_split.items()}


def energize_fastmap(mapp, fastmap, pos, dir):
    visited, split = energize_to_split(mapp, pos, dir)
    if split is not None:
        visited |= fastmap[split]
    return visited


def solve(inp, part1):
    mapp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    if part1:
        return len(energize(mapp, Vec(-1, 0), RIGHT))
    else:
        fastmap = build_fastmap(mapp)
        xmax, ymax = map(max, zip(*mapp.keys()))
        starts = [(Vec(-1, y), RIGHT) for y in range(ymax + 1)] + \
                 [(Vec(xmax + 1, y), LEFT) for y in range(ymax + 1)] + \
                 [(Vec(x, -1), DOWN) for x in range(xmax + 1)] + \
                 [(Vec(x, ymax + 1), UP) for x in range(xmax + 1)]
        return max(len(energize_fastmap(mapp, fastmap, p, d)) for p, d in starts)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
