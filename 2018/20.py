from aoc_utils import Vec


def parse(inp):
    parts = []
    res = []
    starts = []
    for i, c in enumerate(inp):
        if c in "NSEW" and not starts:
            res.append(inp[i])
        if c in ")|" and len(starts) == 1:
            parts.append(parse(inp[starts[0] + 1:i]))
            starts[0] = i
            if c == ")":
                res.append(tuple(parts))
                parts = []
        if c == "(":
            starts.append(i)
        if c == ")":
            starts.pop()
    return res


dirs = {
    "N": Vec(0, -1),
    "S": Vec(0, 1),
    "E": Vec(1, 0),
    "W": Vec(-1, 0),
}


def explore(positions, path, rooms, doors):
    for step in path:
        if isinstance(step, tuple):
            new_positions = set()
            for p in step:
                res = explore(positions, p, rooms, doors)
                new_positions |= res
            positions = new_positions
        elif step in dirs:
            for pos in positions:
                rooms.add(pos + dirs[step])
                doors.add((pos, pos + dirs[step]))
                doors.add((pos + dirs[step], pos))
            positions = {pos + dirs[step] for pos in positions}
        else:
            assert False
    return positions


def solve(inp, part1):
    path = parse(inp[1:-1])
    rooms = {Vec(0, 0)}
    doors = set()
    explore(rooms.copy(), path, rooms, doors)

    edge = {Vec(0, 0)}
    visited = {Vec(0, 0): 0}
    while edge:
        visited |= edge
        new_edge = set()
        for p in edge:
            for d in dirs.values():
                if (p, p + d) in doors and p + d not in visited:
                    new_edge.add(p + d)
                    visited[p + d] = visited[p] + 1
        edge = new_edge

    if part1:
        return max(visited.values())
    else:
        return sum(l >= 1000 for l in visited.values())


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
