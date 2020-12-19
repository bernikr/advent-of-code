from aocd import get_data


def part1(a):
    degrees_to_dir = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    dir_to_coordinates = {'N': (1, 0, 0), 'S': (-1, 0, 0), 'E': (1, 0, 0), 'W': (-1, 0, 0), 'R': (0, 0, 1), 'L': (0, 0, -1)}

    x, y, dir = 0, 0, 90
    for c, n in a:
        if c == 'F':
            c = degrees_to_dir[dir]
        dx, dy, ddir = dir_to_coordinates[c]
        x += dx*n
        y += dy*n
        dir += ddir*n
        if dir < 0:
            dir += 360
        elif dir >= 360:
            dir -= 360
    return abs(x)+abs(y)


def part2(a):
    dir_to_coordinates = {'N': (1, 0), 'S': (-1, 0), 'E': (0, 1), 'W': (0, -1)}

    x, y, wx, wy = 0, 0, 1, 10
    for c, n in a:
        if c == 'F':
            x += wx*n
            y += wy*n
        elif c == 'R' or c == 'L':
            if c == 'L':
                n *= -1
            if n < 0:
                n += 360
            n = int(n/90)
            for _ in range(n):
                wx, wy = -wy, wx
        else:
            dx, dy = dir_to_coordinates[c]
            wx += dx*n
            wy += dy*n
    return abs(x)+abs(y)


if __name__ == '__main__':
    data = get_data(day=12, year=2020)
    inp = [(l[0], int(l[1:])) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
