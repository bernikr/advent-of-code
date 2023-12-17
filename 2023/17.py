from aoc_utils import a_star


def get_neighbor_function(xmax, ymax, step_min, step_max):
    def n(state):
        x, y, dx, dy, moved = state
        if moved < step_max:
            if 0 <= x + dx <= xmax and 0 <= y + dy <= ymax:
                yield x + dx, y + dy, dx, dy, moved + 1
        if moved >= step_min:
            if 0 <= x + dy <= xmax and 0 <= y - dx <= ymax:
                yield x + dy, y - dx, dy, -dx, 1
            if 0 <= x - dy <= xmax and 0 <= y + dx <= ymax:
                yield x - dy, y + dx, -dy, dx, 1

    return n


def solve(inp, part1):
    step_min, step_max = (0, 3) if part1 else (4, 10)
    mapp = [[int(x) for x in l] for l in inp.splitlines()]
    starts = {(0, 0, 1, 0, 0), (0, 0, 0, 1, 0)}  # x, y, dx, dy, moves
    goal = (len(mapp[0]) - 1, len(mapp) - 1)
    is_goal = lambda s: s[0] == goal[0] and s[1] == goal[1] and s[4] >= step_min
    neighbors = get_neighbor_function(*goal, step_min, step_max)
    d = lambda c, n: mapp[n[1]][n[0]]
    h = lambda s: goal[0] - s[0] + goal[1] - s[1]
    return a_star(starts, is_goal, neighbors, d, h)[1]


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
