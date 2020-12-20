from aocd import get_data


def part1(a):
    visited_houses = {(0, 0)}
    x, y = 0, 0
    for c in a:
        if c == '^':
            x += 1
        elif c == 'v':
            x -= 1
        elif c == '<':
            y -= 1
        elif c == '>':
            y += 1
        visited_houses.add((x, y))
    return len(visited_houses)


def part2(a):
    visited_houses = {(0, 0)}
    x, y, rx, ry = 0, 0, 0, 0
    for i, c in enumerate(a):
        dx, dy = 0, 0
        if c == '^':
            dx = 1
        elif c == 'v':
            dx = -1
        elif c == '<':
            dy = -1
        elif c == '>':
            dy = 1
        if i % 2 == 0:
            x += dx
            y += dy
            visited_houses.add((x, y))
        else:
            rx += dx
            ry += dy
            visited_houses.add((rx, ry))
    return len(visited_houses)


if __name__ == '__main__':
    data = get_data(day=3, year=2015)
    inp = data
    print(part1(inp))
    print(part2(inp))
