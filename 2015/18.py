import itertools

from aocd import get_data

directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]


def simulate(m, rounds, stuck_corners=False):
    def neighbors(m, x, y):
        return [m[x + i][y + j] for i, j in directions if 0 <= x + i < len(m) and 0 <= y + j < len(m[x])].count('#')

    rules = {
        '.': lambda m, x, y: '#' if neighbors(m, x, y) == 3 else '.',
        '#': lambda m, x, y: '#' if 2 <= neighbors(m, x, y) <= 3 else '.'
    }

    new = m
    for i in range(rounds):
        old = new
        new = [[rules[s](old, x, y) for y, s in enumerate(row)] for x, row in enumerate(old)]
        if stuck_corners:
            for x, y in itertools.product([0, 99], repeat=2):
                new[x][y] = '#'
    return new


def part1(a):
    return sum(row.count('#') for row in simulate(a, 100))


def part2(a):
    return sum(row.count('#') for row in simulate(a, 100, True))


if __name__ == '__main__':
    data = get_data(day=18, year=2015)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
