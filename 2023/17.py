from aoc_utils import a_star


def get_neighbor_function(mapp, xmax, ymax, step_min, step_max):
    def n(state):
        x, y, dx, dy = state
        sum_a, sum_b = 0, 0
        for i in range(1, step_max + 1):
            if 0 <= x + dy * i <= xmax and 0 <= y - dx * i <= ymax:
                sum_a += mapp[y - dx * i][x + dy * i]
                if i >= step_min:
                    yield (x + dy * i, y - dx * i, dy, -dx), sum_a
            if 0 <= x - dy * i <= xmax and 0 <= y + dx * i <= ymax:
                sum_b += mapp[y + dx * i][x - dy * i]
                if i >= step_min:
                    yield (x - dy * i, y + dx * i, -dy, dx), sum_b

    return n


def solve(inp, part1):
    step_min, step_max = (1, 3) if part1 else (4, 10)
    mapp = [[int(x) for x in l] for l in inp.splitlines()]
    starts = {(0, 0, 1, 0), (0, 0, 0, 1)}  # x, y, dx, dy
    goal = (len(mapp[0]) - 1, len(mapp) - 1)
    is_goal = lambda s: s[0] == goal[0] and s[1] == goal[1]
    neighbors = get_neighbor_function(mapp, *goal, step_min, step_max)
    h = lambda s: goal[0] - s[0] + goal[1] - s[1]
    path, cost = a_star(starts, is_goal, neighbors, h=h)
    return cost


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
