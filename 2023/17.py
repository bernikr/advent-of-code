import math
from collections import defaultdict
from itertools import pairwise

from aoc_utils import Vec, Dir, PriorityQueue


def get_neighbor_function(mapp):
    def n(state):
        pos, dir, moved = state
        steps = []
        if moved < 3:
            steps.append((dir, moved + 1))
        steps.append((dir.turn_left(), 1))
        steps.append((dir.turn_right(), 1))
        return [(pos + d.value, d, m) for d, m in steps if pos + d.value in mapp]

    return n


def get_neighbor_function_part2(mapp):
    def n(state):
        pos, dir, moved = state
        steps = []
        if moved < 10:
            steps.append((dir, moved + 1))
        if moved >= 4:
            steps.append((dir.turn_left(), 1))
            steps.append((dir.turn_right(), 1))
        return [(pos + d.value, d, m) for d, m in steps if pos + d.value in mapp]

    return n


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


def a_star(starts, is_goal, h, get_neighbors, d):
    open_set = PriorityQueue()
    g_score = defaultdict(lambda: math.inf)
    came_from = {}
    seen = set()

    for s in starts:
        open_set.put(s, h(s))
        g_score[s] = 0

    while open_set:
        current = open_set.get()
        if current in seen:
            continue
        seen.add(current)
        if is_goal(current):
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + d(current, neighbor)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                open_set.put(neighbor, tentative_g_score + h(neighbor))


def solve(inp, part1):
    mapp = {Vec(x, y): int(c) for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    starts = {(Vec(0, 0), Dir.RIGHT, 0), (Vec(0, 0), Dir.DOWN, 0)}
    goal = Vec(*map(max, zip(*mapp.keys())))
    is_goal = lambda s: s[0] == goal and (part1 or s[2] >= 4)
    h = lambda s: (s[0] - goal).manhatten()
    neighbors = get_neighbor_function(mapp) if part1 else get_neighbor_function_part2(mapp)
    d = lambda c, n: mapp[n[0]]
    shortest_path = a_star(starts, is_goal, h, neighbors, d)
    return sum(d(a, b) for a, b in pairwise(shortest_path))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
