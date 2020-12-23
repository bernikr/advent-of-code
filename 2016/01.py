from aocd import get_data


def part1(a):
    dir = 0
    x, y = 0, 0
    for d, n in a:
        if d == "R":
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4

        if dir >= 2:
            n *= -1

        if dir % 2 == 0:
            x += n
        else:
            y += n

    return abs(x) + abs(y)


def part2(a):
    dir = 0
    x, y = 0, 0
    visited = {(0, 0)}
    for d, n in a:
        if d == "R":
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4

        for _ in range(n):
            step = -1 if dir >= 2 else 1

            if dir % 2 == 0:
                x += step
            else:
                y += step
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))


if __name__ == '__main__':
    data = get_data(day=1, year=2016)
    inp = [(l[0], int(l[1:])) for l in data.split(', ')]
    print(part1(inp))
    print(part2(inp))
