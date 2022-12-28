import itertools

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


def solve(inp, part1):
    inp = inp.splitlines()
    return sum(row.count('#') for row in simulate(inp, 100, not part1))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
