from collections import defaultdict, Counter

from aocd import get_data


def distance(i, j):
    return sum(abs(a-b) for a, b in zip(i, j))


def closest(c, l):
    next_points = sorted(((i, distance(c, x)) for i, x in enumerate(l)), key=lambda x: x[1])
    if next_points[0][1] == next_points[1][1]:
        return None
    else:
        return next_points[0][0]


def part1(a):
    area = {}
    infinite_areas = set()
    x_min, x_max = min(x[0] for x in a), max(x[0] for x in a)
    y_min, y_max = min(x[1] for x in a), max(x[1] for x in a)
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            area[(i, j)] = closest((i, j), a)
            if i == x_min or i == x_max or j == y_min or j == y_max:
                infinite_areas.add(area[(i, j)])
    return max(c for a, c in Counter(area.values()).items() if a not in infinite_areas)


def part2(a):
    area = {}
    x_min, x_max = min(x[0] for x in a), max(x[0] for x in a)
    y_min, y_max = min(x[1] for x in a), max(x[1] for x in a)
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            area[(i, j)] = sum(distance((i, j), c) for c in a) < 10000
    return sum(area.values())


if __name__ == '__main__':
    data = get_data(day=6, year=2018)
    inp = [tuple(map(int, l.split(', '))) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
