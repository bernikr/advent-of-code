directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]


def simulate(m, limit, neighbors_function):
    rules = {
        '.': lambda m, x, y: '.',
        'L': lambda m, x, y: '#' if neighbors_function(m, x, y) == 0 else 'L',
        '#': lambda m, x, y: 'L' if neighbors_function(m, x, y) >= limit else '#'
    }

    new = m
    old = []
    while new != old:
        old = new
        new = [[rules[s](old, x, y) for y, s in enumerate(row)] for x, row in enumerate(old)]
    return sum(row.count('#') for row in new)


def neighbors1(m, x, y):
    return [m[x + i][y + j] for i, j in directions if 0 <= x + i < len(m) and 0 <= y + j < len(m[x])].count('#')


def part1(a):
    return simulate(a, 4, neighbors1)


def neighbors2(m, x, y):
    return [next((m[x + i * a][y + j * a] for a in range(1, max(len(m), len(m[x]))) if
                  0 <= x + i * a < len(m) and 0 <= y + j * a < len(m[x]) and m[x + i * a][y + j * a] != '.'), '.') for
            i, j in directions].count('#')


def part2(a):
    return simulate(a, 5, neighbors2)


def solve(inp, ispart1):
    inp = inp.splitlines()
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
