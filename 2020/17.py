import itertools
import operator

from aocd import get_data


def simulate(start_set, neighbor_function, rule_function, rounds):
    active = start_set
    for i in range(rounds):
        next_active = set()
        empty_neighbors = set()
        for cell in active:
            neighbors = neighbor_function(cell)
            empty_neighbors.update(c for c in neighbors if c not in active)
            num = sum(c in active for c in neighbors)
            if rule_function(num, True):
                next_active.add(cell)
        for cell in empty_neighbors:
            num = sum(c in active for c in neighbor_function(cell))
            if rule_function(num, False):
                next_active.add(cell)
        active = next_active
    return active


def rules(num, active):
    if active:
        return 2 <= num <= 3
    else:
        return num == 3


def neighbors3d(c):
    return [tuple(map(operator.add, c, n)) for n in itertools.product([-1, 0, 1], repeat=3) if not n == (0, 0, 0)]


def part1(a):
    start = set()
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] == '#':
                start.add((x, y, 0))
    return len(simulate(start, neighbors3d, rules, 6))


def neighbors4d(c):
    return [tuple(map(operator.add, c, n)) for n in itertools.product([-1, 0, 1], repeat=4) if not n == (0, 0, 0, 0)]


def part2(a):
    start = set()
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] == '#':
                start.add((x, y, 0, 0))
    return len(simulate(start, neighbors4d, rules, 6))


if __name__ == '__main__':
    data = get_data(day=17, year=2020)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
