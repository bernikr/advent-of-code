from aoc_utils import Vec, Dir, a_star


def get_neighbor_function(mapp, part1):
    def n(state):
        pos, dir, moved = state
        steps = []
        if moved < (3 if part1 else 10):
            steps.append((dir, moved + 1))
        if moved >= (0 if part1 else 4):
            steps.append((dir.turn_left(), 1))
            steps.append((dir.turn_right(), 1))
        return [(pos + d.value, d, m) for d, m in steps if pos + d.value in mapp]

    return n


def solve(inp, part1):
    mapp = {Vec(x, y): int(c) for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    starts = {(Vec(0, 0), Dir.RIGHT, 0), (Vec(0, 0), Dir.DOWN, 0)}
    goal = Vec(*map(max, zip(*mapp.keys())))
    is_goal = lambda s: s[0] == goal and (part1 or s[2] >= 4)
    neighbors = get_neighbor_function(mapp, part1)
    d = lambda c, n: mapp[n[0]]
    h = lambda s: (s[0] - goal).manhatten()
    shortest_path, cost = a_star(starts, is_goal, neighbors, d, h)
    return cost


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
